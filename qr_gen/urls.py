from django.urls import path
from .views import mehrum

urlpatterns = [
    path('<int:id>/', mehrum)
]