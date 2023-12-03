from django.shortcuts import render
from rest_framework import generics
from vendors.models import Vendor
from vendors.serializers import VendorSerializer

# Create your views here.


class VendorListView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    

class VendorActionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
