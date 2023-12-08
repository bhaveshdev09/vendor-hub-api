import datetime
from orders.models import PurchaseOrder
from orders.constants import OrderStatus
from orders import signals
from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.utils.translation import gettext as _
from django.utils import timezone


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        exclude = ["created_at", "updated_at"]
        extra_kwargs = {
            "po_number": {
                "error_messages": {
                    "required": _("please provide number of purchase order")
                }
            },
            "order_date": {
                "error_messages": {"required": _("please provide order date")}
            },
            "delivery_date": {
                "error_messages": {"required": _("please provide delivery date")}
            },
            "quantity": {
                "error_messages": {"required": _("please provide total item quantity")}
            },
            "quality_ratings": {"max_value": 10.00, "min_value": 0.0},
            "vendor": {"error_messages": {"required": _("please provide vendor Id")}},
        }

    def validate(self, attrs):
        # if instance.status == validated_data.get("status") == OrderStatus.COMPLETED:
        #     raise ValidationError(
        #         _("Purchase order status already marked as completed")
        #     )
        return super().validate(attrs)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if instance.status == OrderStatus.COMPLETED:
            signals.purchase_order_status_completed.send(
                sender=instance.__class__, instance=instance
            )
        return instance


class PurchaseOrderAcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ["acknowledgment_date"]
        extra_kwargs = {"acknowledgment_date": {"required": True}}

    def validate_acknowledgment_date(self, value):
        if not value:
            value = timezone.now()
        return value

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        signals.purchase_order_acknowledged.send(
            sender=instance.__class__, instance=instance
        )
        return instance
