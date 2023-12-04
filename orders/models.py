from django.db import models
from django.urls import reverse
from vendors.models import Vendor, BaseModel
from vms_project.shortcuts import get_random_code


# Create your models here.
class PurchaseOrder(BaseModel):
    STATUS_PENDING = "pending"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"
    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STATUS_COMPLETED, "completed"),
        (STATUS_CANCELLED, "cancelled"),
    )
    po_number = models.CharField(max_length=12, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    quality_rating = models.FloatField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.po_number} - {self.vendor.name}"

    def get_absolute_url(self):
        return reverse("orders:purchase-order-actions", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-order_date"]
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"
