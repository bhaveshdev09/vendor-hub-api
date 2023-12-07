from rest_framework import serializers
from django.utils.translation import gettext as _
from vendors.models import Vendor, HistoricalPerformance


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"
        read_only_fields = [
            "id",
            "vendor_code",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "name": {
                "error_messages": {"required": _("please provide name of vendor")}
            },
            "contact_details": {
                "error_messages": {
                    "required": _("please provide vendor contact details")
                }
            },
            "address": {
                "error_messages": {"required": _("please provide vendor address")}
            },
        }


class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]


class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = "__all__"
