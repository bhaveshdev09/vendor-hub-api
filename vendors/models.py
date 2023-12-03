import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from vms_project.shortcuts import get_random_code


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Vendor(BaseModel):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(
        max_length=50, unique=True, default=get_random_code, editable=False
    )
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    class Meta:
        verbose_name = _("vendor")
        verbose_name_plural = _("vendors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vendor-details", kwargs={"pk": self.pk})
