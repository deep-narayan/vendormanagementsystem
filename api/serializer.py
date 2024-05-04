from rest_framework import serializers
from .models import Vendor, PurchaseOrder, PerformanceModel

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PerformanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceModel
        fields = '__all__'
