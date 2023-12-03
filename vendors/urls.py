from django.urls import path, include
from vendors import views

app_name = "vendors"

urlpatterns = [
    path("", views.VendorListView.as_view(), name="vendors-list"),
    path("<uuid:pk>/", views.VendorActionView.as_view(), name="vendors-action"),
]
