# tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import PurchaseOrder, Vendor
from .serializers import PurchaseOrderSerializer


class PurchaseOrderTests(APITestCase):
    def setUp(self):
        # Create a vendor for testing
        self.vendor_data = {
            "name": "rahul",
            "contact_details": "test contact details of rahul",
            "address": "test address of rahul",
        }
        self.vendor = Vendor.objects.create(**self.vendor_data)
        self.client = APIClient()

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

        self.purchase_order = PurchaseOrder.objects.create(
            vendor=self.vendor, **self.po_data
        )
        self.purchase_order_url = reverse("orders:purchase-order-list")

    def test_purchase_order_model(self):
        self.assertTrue(isinstance(self.purchase_order, PurchaseOrder))
        self.assertEqual(
            str(self.purchase_order),
            f"{self.purchase_order.po_number} - {self.purchase_order.vendor}",
            "Object str representaion mismatch",
        )

    def test_model_url(self):
        response = self.client.get(self.purchase_order.get_absolute_url())
        self.assertEqual(
            response.status_code, 200, "Invalid absolute url configuration"
        )

    def test_create_purchase_order(self):
        self.new_po_data = {
            "po_number": "PO54321",
            "vendor": self.vendor.id,
            "order_date": "2023-12-10T14:00:00Z",
            "delivery_date": "2023-12-20T14:00:00Z",
            "items": [
                {"item_name": "Product C", "quantity": 15, "unit_price": 19.99},
                {"item_name": "Material D", "quantity": 30, "unit_price": 7.5},
            ],
            "quantity": 45,
            "status": "pending",
            "quality_rating": None,
            "issue_date": "2023-12-01T08:00:00Z",
            "acknowledgment_date": None,
        }

        response = self.client.post(
            self.purchase_order_url, data=self.new_po_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 2)

    def test_create_purchase_order_blank_data(self):
        self.new_po_data = {}

        response = self.client.post(
            self.purchase_order_url, data=self.new_po_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrder.objects.count(), 1)

    def test_list_purchase_orders(self):
        response = self.client.get(self.purchase_order_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)

    def test_retrieve_purchase_order(self):
        detail_url = reverse(
            "orders:purchase-order-actions", args=[self.purchase_order.id]
        )
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["po_number"], self.po_data["po_number"])

    def test_update_purchase_order(self):
        update_data = {
            "po_number": "PO67890",
            "order_date": "2023-12-05T10:30:00Z",
            "delivery_date": "2023-12-15T10:30:00Z",
            "status": "completed",
        }
        detail_url = reverse(
            "orders:purchase-order-actions", args=[self.purchase_order.id]
        )
        response = self.client.patch(detail_url, data=update_data, format="json")  # put and patch request
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.purchase_order.refresh_from_db()
        self.assertEqual(self.purchase_order.po_number, update_data["po_number"])
        self.assertEqual(self.purchase_order.status, update_data["status"])

    def test_delete_purchase_order(self):
        detail_url = reverse(
            "orders:purchase-order-actions", args=[self.purchase_order.id]
        )
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PurchaseOrder.objects.count(), 0)
