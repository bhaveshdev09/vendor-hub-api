from django.db import models
from django.urls import reverse
from vendors.models import Vendor, BaseModel
from orders.constants import OrderStatus


# Create your models here.
class PurchaseOrder(BaseModel):
    STATUS_CHOICES = (
        (OrderStatus.PENDING, "pending"),
        (OrderStatus.COMPLETED, "completed"),
        (OrderStatus.CANCELLED, "cancelled"),
    )
    po_number = models.CharField(max_length=12, unique=True)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="purchase_orders"
    )
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    issue_date = models.DateTimeField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    quality_rating = models.FloatField(null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=OrderStatus.PENDING
    )

    def __str__(self):
        return f"{self.po_number} - {self.vendor.name}"

    def get_absolute_url(self):
        return reverse("orders:purchase-order-actions", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-order_date"]
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"
