from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from vendors.models import Vendor
from orders.models import PurchaseOrder

User = get_user_model()


class PurchaseOrderTests(APITestCase):
    def setUp(self):
        # Create a vendor for testing
        self.user = User.objects.create(email="test@test.com", password="test@123")
        self.vendor_data = {
            "name": "rahul",
            "contact_details": "test contact details of rahul",
            "address": "test address of rahul",
        }
        self.vendor = Vendor.objects.create(**self.vendor_data)
        self.model = PurchaseOrder
        self.client = APIClient()  # Authenticated user
        self.client.force_authenticate(user=self.user)
        self.anonymous_client = APIClient()  # Unauthenticated user

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
        self.purchase_order_url = reverse("orders:purchase-order-list")

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
        self.assertEqual(self.model.objects.count(), 2)

    def test_create_purchase_order_with_anonymous_user(self):
        self.new_po_data = {
            "po_number": "PO54324",
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

        response = self.anonymous_client.post(
            self.purchase_order_url, data=self.new_po_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )
        self.assertEqual(self.model.objects.count(), 1)

    def test_create_purchase_order_blank_data(self):
        self.new_po_data = {}
        response = self.client.post(
            self.purchase_order_url, data=self.new_po_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.model.objects.count(), 1)

    def test_list_purchase_orders(self):
        response = self.client.get(self.purchase_order_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)

    def test_list_purchase_orders_with_anonymous_user(self):
        response = self.anonymous_client.get(self.purchase_order_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )

    def test_retrieve_purchase_order(self):
        detail_url = reverse(
            "orders:purchase-order-actions", args=[self.purchase_order.id]
        )
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["po_number"], self.po_data["po_number"])

    def test_retrieve_purchase_order_with_anonymous_user(self):
        detail_url = reverse(
            "orders:purchase-order-actions", args=[self.purchase_order.id]
        )
        response = self.anonymous_client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )

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
        response = self.client.patch(
            detail_url, data=update_data, format="json"
        )  # put and patch request
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.purchase_order.refresh_from_db()
        self.assertEqual(self.purchase_order.po_number, update_data["po_number"])
        self.assertEqual(self.purchase_order.status, update_data["status"])

    def test_update_purchase_order_with_anonymous_user(self):
        update_data = {
            "po_number": "PO67890",
            "order_date": "2023-12-05T10:30:00Z",
            "delivery_date": "2023-12-15T10:30:00Z",
            "status": "completed",
        }
        detail_url = reverse(
            "orders:purchase-order-actions", args=[self.purchase_order.id]
        )
        response = self.anonymous_client.patch(
            detail_url, data=update_data, format="json"
        )  # put and patch request
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )

    def test_delete_purchase_order(self):
        detail_url = reverse(
            "orders:purchase-order-actions", args=[self.purchase_order.id]
        )
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.model.objects.count(), 0)

    def test_delete_purchase_order_with_anonymous_user(self):
        detail_url = reverse(
            "orders:purchase-order-actions", args=[self.purchase_order.id]
        )
        response = self.anonymous_client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )

    def test_acknowledge_purchase_order(self):
        # Make a POST request to the acknowledgment endpoint
        detail_url = reverse(
            "orders:purchase-order-acknowledge", args=[self.purchase_order.id]
        )
        response = self.client.put(
            detail_url, data={"acknowledgment_date": None}, format="json"
        )
        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get("code"), "success_acknowledgement")
        # Check if acknowledgment_date is updated in the purchase order
        self.purchase_order.refresh_from_db()
        self.assertIsNotNone(self.purchase_order.acknowledgment_date)

    def test_acknowledge_purchase_order_with_anonymous_user(self):
        # Make a POST request to the acknowledgment endpoint
        detail_url = reverse(
            "orders:purchase-order-acknowledge", args=[self.purchase_order.id]
        )
        response = self.anonymous_client.put(
            detail_url, data={"acknowledgment_date": None}, format="json"
        )
        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            getattr(response.data.get("detail"), "code"), "not_authenticated"
        )
