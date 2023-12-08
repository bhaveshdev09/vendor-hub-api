from django.test import TestCase
from django.urls import reverse
from vendors.models import Vendor, HistoricalPerformance


class VendorModelTestCase(TestCase):
    def setUp(self):
        self.model = Vendor
        # Create a vendor model for testing
        self.vendor_data = {
            "name": "rahul",
            "contact_details": "test contact details of rahul",
            "address": "test address of rahul",
        }
        self.vendor = self.model.objects.create(**self.vendor_data)
        self.vendor_url = self.vendor.get_absolute_url()

    def test_model_instance(self):
        self.assertIsInstance(self.vendor, self.model)
        self.assertEqual(
            str(self.vendor),
            self.vendor_data.get("name"),
            "mismatch model string representaion",
        )

    def test_model_absolute_url(self):
        expected_model_url = reverse(
            "vendors:vendor-actions", kwargs={"pk": self.vendor.pk}
        )
        self.assertEqual(self.vendor_url, expected_model_url, "Invalid url")

    def test_method_get_purchase_orders_by_status_by_providing_non_status_value(self):
        filter_purchase_orders = self.vendor.get_purchase_orders_by_status(
            status="incomplete"
        )
        self.assertIsNone(filter_purchase_orders)

    def test_calc_on_time_delivery_rate_for_zero_divison_error_returned_value(self):
        on_time_delivery_rate = self.vendor.calc_on_time_delivery_rate()
        self.assertEqual(on_time_delivery_rate, 0)

    def test_calc_fullfillment_for_zero_divison_error_returned_value(self):
        fulfillment_rate = self.vendor.calc_fulfillment_rate()
        self.assertEqual(fulfillment_rate, 0)

    def test_calc_avg_response_time_returned_value(self):
        avg_response_time = self.vendor.calc_avg_response_time()
        self.assertEqual(avg_response_time, 0)


class HistoricalPerformanceTestCase(TestCase):
    def setUp(self):
        self.model = HistoricalPerformance
        self.vendor_model = Vendor
        self.vendor_data = {
            "name": "rahul",
            "contact_details": "test contact details of rahul",
            "address": "test address of rahul",
        }
        self.vendor = self.vendor_model.objects.create(**self.vendor_data)

        self.vendor_performance_data = {
            "vendor": self.vendor,
            "on_time_delivery_rate": 95.0,
            "quality_rating_avg": 4.5,
            "average_response_time": 2.5,
            "fulfillment_rate": 98.0,
        }
        self.performance_history = self.model.objects.create(
            **self.vendor_performance_data
        )

    def test_model_instance(self):
        self.assertIsInstance(self.performance_history, self.model)
        self.assertEqual(
            str(self.performance_history),
            f"{self.vendor.name} - {self.performance_history.history_date}",
            "mismatch model string representaion",
        )
