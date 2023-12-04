from rest_framework import generics
from orders.models import PurchaseOrder
from orders.serializers import PurchaseOrderSerializer


class PurchaseOrderListView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderActionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
