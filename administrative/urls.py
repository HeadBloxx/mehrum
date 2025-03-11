from django.urls import path
from .views import download_qr

urlpatterns = [
    path("admin/download_qr/<int:obj_id>/", download_qr, name="download_qr"),
]
