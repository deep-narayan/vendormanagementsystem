from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.vendors),
    path('vendors/<int:vendor_id>/', views.vendor_detail),
    path('purchase_orders/', views.purchase_orders),
    path('purchase_orders/<int:po_id>/', views.purchase_order_detail),
    path('vendors/<int:vendor_id>/performance/', views.vendor_performance),
    path('purchase_orders/<int:po_id>/acknowledge', views.acknowledge_purchase_order),
]

