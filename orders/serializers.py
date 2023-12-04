from django.utils.translation import gettext as _
from orders.models import PurchaseOrder
from vendors.serializers import Vendor, serializers


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
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
            "vendor": {"error_messages": {"required": _("please provide vendor Id")}},
        }
