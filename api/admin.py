from django.contrib import admin
from .models import Vendor, PurchaseOrder, PerformanceModel

admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(PerformanceModel)

