from django.test import TestCase
from orders.models import PurchaseOrder
from orders.serializers import PurchaseOrderAcknowledgeSerializer
from django.utils import timezone
from django.db.models import signals
from vendors.models import Vendor
from orders.models import PurchaseOrder


class PurchaseOrderAcknowledgeSerializerTestCase(TestCase):
    def setUp(self):
        self.vendor_data = {
            "name": "rahul",
            "contact_details": "test contact details of rahul",
            "address": "test address of rahul",
        }
        self.vendor = Vendor.objects.create(**self.vendor_data)
        self.po_data = {
            "po_number": "PO54321",
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
        self.purchase_order = PurchaseOrder.objects.create(
            vendor=self.vendor, **self.po_data
        )

    def test_valid_acknowledge_date(self):
        serializer = PurchaseOrderAcknowledgeSerializer(
            instance=self.purchase_order,
            data={"acknowledgment_date": "2023-01-01T12:00:00Z"},
        )
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.purchase_order.refresh_from_db()
        self.assertEqual(
            self.purchase_order.acknowledgment_date,
            timezone.datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc),
        )

    def test_missing_acknowledge_date(self):
        # Test that if acknowledgment_date is not provided, it defaults to the current time
        serializer = PurchaseOrderAcknowledgeSerializer(
            instance=self.purchase_order, data={}
        )
        self.assertFalse(serializer.is_valid())

    def test_null_acknowledge_date(self):
        # Test that if acknowledgment_date is not provided, it defaults to the current time
        serializer = PurchaseOrderAcknowledgeSerializer(
            instance=self.purchase_order, data={"acknowledgment_date": None}
        )
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.purchase_order.refresh_from_db()
        self.assertIsNotNone(self.purchase_order.acknowledgment_date)

    def test_update_method(self):
        # Test the update method behavior
        serializer = PurchaseOrderAcknowledgeSerializer(
            instance=self.purchase_order,
            data={"acknowledgment_date": "2023-01-02T12:00:00Z"},
        )
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.purchase_order.refresh_from_db()
        self.assertEqual(
            self.purchase_order.acknowledgment_date,
            timezone.datetime(2023, 1, 2, 12, 0, 0, tzinfo=timezone.utc),
        )
