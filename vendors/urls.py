from django.urls import path
from vendors import views

app_name = "vendors"

urlpatterns = [
    path("", views.VendorListView.as_view(), name="vendors-list"),
    path("<uuid:pk>/", views.VendorActionView.as_view(), name="vendor-actions"),
    path(
        "<uuid:pk>/performance",
        views.VendorPerformanceView.as_view(),
        name="vendor-performance",
    ),
    path(
        "<uuid:pk>/performance-history",
        views.VendorPerformanceHistoryView.as_view(),
        name="vendor-performance-history",
    ),
]
