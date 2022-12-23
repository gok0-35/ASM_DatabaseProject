from django.urls import path
from . import views

# http://127.0.0.1:8000/

urlpatterns = [
   path("", views.WelcomePage, name='WelcomePage'),
   path("medicalSupplies", views.medicalSupplies, name='medicalSupplies'),
   path("foodSupplies", views.foodSupplies, name='foodSupplies'),
   path("electronicSupplies", views.electronicSupplies, name='electronicSupplies'),
   path("cleaningSupplies", views.cleaningSupplies, name='cleaningSupplies'),
]