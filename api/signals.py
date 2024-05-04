from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import PurchaseOrder, PerformanceModel, Vendor
from django.db import transaction

@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, created, **kwargs):
    if created:
        vendor = instance.vendor
        total_orders = vendor.purchaseorder_set.count()
        completed_orders = vendor.purchaseorder_set.filter(status='completed').count()
        on_time_delivery_rate = completed_orders / total_orders if total_orders > 0 else 0

        quality_rating_avg = vendor.purchaseorder_set.filter(quality_rating__isnull=False).aggregate(Avg('quality_rating'))['quality_rating__avg']

        total_response_time = 0
        for order in vendor.purchaseorder_set.filter(acknowledgment_date__isnull=False):
            total_response_time += (order.acknowledgment_date - order.issue_date).total_seconds()
        average_response_time = total_response_time / completed_orders if completed_orders > 0 else 0

        fulfilled_orders = vendor.purchaseorder_set.filter(status='completed', quality_rating__isnull=False).count()
        fulfillment_rate = fulfilled_orders / total_orders if total_orders > 0 else 0

        with transaction.atomic():
            performance = PerformanceModel.objects.create(vendor=vendor, on_time_delivery_rate=on_time_delivery_rate,
                                                          quality_rating_avg=quality_rating_avg,
                                                          average_response_time=average_response_time,
                                                          fulfillment_rate=fulfillment_rate)
            vendor.on_time_delivery_rate = on_time_delivery_rate
            vendor.quality_rating_avg = quality_rating_avg
            vendor.average_response_time = average_response_time
            vendor.fulfillment_rate = fulfillment_rate
            vendor.save()

@receiver(pre_delete, sender=PurchaseOrder)
def delete_performance_metrics(sender, instance, **kwargs):
    vendor = instance.vendor
    performance = vendor.performancemodel_set.last()
    if performance:
        with transaction.atomic():
            vendor.on_time_delivery_rate = 0
            vendor.quality_rating_avg = 0
            vendor.average_response_time = 0
            vendor.fulfillment_rate = 0
            vendor.save()
            performance.delete()
