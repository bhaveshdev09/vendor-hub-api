from django.test import TestCase
from vendors.models import Vendor, HistoricalPerformance
from vendors.serializers import VendorSerializer, HistoricalPerformanceSerializer


class VendorSerializerTestCase(TestCase):
    def setUp(self):
        self.vendor_data = {
            "name": "Test Vendor",
            "contact_details": "Contact Details",
            "address": "Vendor Address",
            "vendor_code": "test_vendor_code",
            "on_time_delivery_rate": 95.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 2.5,
            "fulfillment_rate": 98.0,
        }
        self.vendor = Vendor.objects.create(**self.vendor_data)

    def test_vendor_serializer(self):
        serializer = VendorSerializer(instance=self.vendor)
        data = serializer.data

        self.assertEqual(data["name"], "Test Vendor")
        self.assertEqual(data["vendor_code"], "test_vendor_code")
        self.assertEqual(data["on_time_delivery_rate"], 95.0)


class HistoricalPerformanceSerializerTestCase(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="Contact Details",
            address="Vendor Address",
        )
        self.performance_data = {
            "vendor": self.vendor,
            "on_time_delivery_rate": 95.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 2.5,
            "fulfillment_rate": 98.0,
        }
        self.performance = HistoricalPerformance.objects.create(**self.performance_data)

    def test_historical_performance_serializer(self):
        serializer = HistoricalPerformanceSerializer(instance=self.performance)
        data = serializer.data

        self.assertEqual(data["vendor"], self.vendor.id)
        self.assertEqual(data["on_time_delivery_rate"], 95.0)
        self.assertEqual(data["quality_rating_avg"], 4.5)
