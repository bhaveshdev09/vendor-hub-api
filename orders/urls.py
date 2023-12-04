from django.urls import path
from orders import views

app_name = "orders"

urlpatterns = [
    path("", views.PurchaseOrderListView.as_view(), name="purchase-order-list"),
    path("<uuid:pk>/", views.PurchaseOrderActionView.as_view(), name="purchase-order-actions"),
]
