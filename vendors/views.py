from rest_framework import generics
from vendors.models import Vendor, HistoricalPerformance
from vendors.serializers import (
    VendorSerializer,
    VendorPerformanceSerializer,
    HistoricalPerformanceSerializer,
)
from rest_framework.permissions import IsAuthenticated


class VendorListView(generics.ListCreateAPIView):
    authentication_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorActionView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer


class VendorPerformanceHistoryView(generics.ListAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
