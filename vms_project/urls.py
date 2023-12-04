from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/vendors/", include("vendors.urls", namespace="vendors")),
    path("api/v1/purchase_orders/", include("orders.urls", namespace="orders")),
]
