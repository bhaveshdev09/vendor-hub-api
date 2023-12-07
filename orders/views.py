from rest_framework import generics

# from drf_spectacular.utils import extend_schema
from orders.models import PurchaseOrder
from orders.serializers import (
    PurchaseOrderSerializer,
    PurchaseOrderAcknowledgeSerializer,
)
from rest_framework.permissions import IsAuthenticated


class PurchaseOrderListView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = (IsAuthenticated,)


class PurchaseOrderActionView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


# Note: Here I have considered put request(for acknowledge po) not post as mentioned in task
class PurchaseOrderAcknowledgeView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderAcknowledgeSerializer
