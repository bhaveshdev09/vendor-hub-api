from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from vendors.models import Vendor


# model & views test
class VendorModelTest(APITestCase):
    def setUp(self):
        self.vendor_data = dict(
            name="rahul",
            contact_details="test contact details of rahul",
            address="test address of rahul",
        )
        self.vendor = Vendor.objects.create(**self.vendor_data)
        self.vendor_url = reverse("vendors:vendor-actions", args=[self.vendor.id])
        self.vendor_create_url = reverse("vendors:vendors-list")
        self.client = APIClient()

    def test_vendor_model(self):
        self.assertTrue(isinstance(self.vendor, Vendor))
        self.assertEqual(
            str(self.vendor),
            self.vendor_data.get("name"),
            "Object str representaion mismatch",
        )

    def test_url(self):
        response = self.client.get(self.vendor_url)
        self.assertEqual(
            response.status_code, 200, "Invalid absolute url configuration"
        )

    def test_list_vendors(self):
        self.vendor_create_url = reverse("vendors:vendors-list")
        response = self.client.get(self.vendor_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)

    def test_create_vendor(self):
        new_vendor_data = {
            "name": "mahesh",
            "contact_details": "test contact details of mahesh",
            "address": "test address of mahesh",
        }
        response = self.client.post(
            self.vendor_create_url, data=new_vendor_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 2)

    def test_create_vendor_blank_data(self):
        new_vendor_data = {
            "name": "",
            "contact_details": "",
            "address": "",
        }
        response = self.client.post(
            self.vendor_create_url, data=new_vendor_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Vendor.objects.count(), 1)

    def test_retrieve_vendor(self):
        response = self.client.get(self.vendor_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.vendor_data["name"])

    def test_update_vendor(self):
        update_data = {
            "name": "vijay",
            "contact_details": "test contact details of vijay",
            "address": "test address of vijay",
        }
        response = self.client.put(self.vendor_url, data=update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendor.refresh_from_db()
        self.assertEqual(self.vendor.name, update_data["name"])

    def test_delete_vendor(self):
        response = self.client.delete(self.vendor_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vendor.objects.count(), 0)
