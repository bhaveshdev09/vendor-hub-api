from django.test import TestCase
from django.urls import reverse
from orders.models import PurchaseOrder
from vendors.models import Vendor


class PurchaseOrderModelTestCase(TestCase):
    def setUp(self):
        self.model = PurchaseOrder
        # Create a vendor model for testing
        self.vendor_data = {
            "name": "rahul",
            "contact_details": "test contact details of rahul",
            "address": "test address of rahul",
        }
        self.vendor = Vendor.objects.create(**self.vendor_data)
        # Create a Purchase Order for testing
        self.po_data = {
            "po_number": "PO12345",
            "order_date": "2023-12-01T08:00:00Z",
            "delivery_date": "2023-12-10T08:00:00Z",
            "items": [{"item_name": "Test Item", "quantity": 5, "unit_price": 10.0}],
            "quantity": 5,
            "status": "pending",
            "quality_rating": None,
            "issue_date": "2023-12-01T08:00:00Z",
            "acknowledgment_date": None,
        }
        self.purchase_order = self.model.objects.create(
            vendor=self.vendor, **self.po_data
        )
        self.purchase_order_url = self.purchase_order.get_absolute_url()
        # self.purchase_order_url = reverse("orders:purchase-order-list")

    def test_model_instance(self):
        self.assertTrue(isinstance(self.purchase_order, self.model))
        self.assertEqual(
            str(self.purchase_order),
            f"{self.purchase_order.po_number} - {self.purchase_order.vendor}",
            "mismatch model string representaion",
        )

    def test_model_absolute_url(self):
        expected_model_url = reverse(
            "orders:purchase-order-actions", kwargs={"pk": self.purchase_order.pk}
        )
        self.assertEqual(self.purchase_order_url, expected_model_url, "Invalid url")




