from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor, PurchaseOrder, PerformanceModel
from .serializer import VendorSerializer, PurchaseOrderSerializer, PerformanceModelSerializer
from django.db.models import Count, Avg
from django.db import transaction
from django.utils import timezone

@api_view(['GET', 'POST'])
def vendors(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    if request.method == 'GET':
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def purchase_orders(request):
    if request.method == 'GET':
        orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def purchase_order_detail(request, po_id):
    order = get_object_or_404(PurchaseOrder, pk=po_id)
    if request.method == 'GET':
        serializer = PurchaseOrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PurchaseOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def vendor_performance(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    performance = vendor.performancemodel_set.last()
    if not performance:
        return Response({"detail": "No performance data available."}, status=status.HTTP_404_NOT_FOUND)
    serializer = PerformanceModelSerializer(performance)
    return Response(serializer.data)


@api_view(['POST'])
def acknowledge_purchase_order(request, po_id):
    order = get_object_or_404(PurchaseOrder, pk=po_id)
    if request.method == 'POST':
        order.acknowledgment_date = timezone.now()
        order.save()
        return Response({"detail": "Purchase order checked successfully."}, status=status.HTTP_200_OK)
