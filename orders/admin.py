from django.contrib import admin
from orders.models import PurchaseOrder


# Register your models here.
class PurchaseOrderAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "po_number",
        "vendor",
        "delivery_date",
        "acknowledgment_date",
        "status",
        "quality_rating",
    ]


admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
