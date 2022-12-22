from django.urls import path
from . import views

# http://127.0.0.1:8000/

urlpatterns = [
   path("", views.WelcomePage, name='WelcomePage'),
   path("MedicalSupplies", views.MedicalSupplies, name='MedicalSupplies'),
   path("foodSupplies", views.foodSupplies, name='foodSupplies'),
   path("electronicSupplies", views.electronicSupplies, name='electronicSupplies'),
   path("cleaningSupplies", views.MedicalSupplies, name='cleaningSupplies'),
   path("AddSupplies", views.AddSupplies, name='AddSupplies')
]