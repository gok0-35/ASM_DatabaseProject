from django.shortcuts import render
from django.http.response import HttpResponse
from .models import MedicalSupplies
from .models import ElectronicSupplies
from .models import CleaningSupplies
from .models import FoodSupplies

# Create your views here.
def WelcomePage(request):
    return render(request, "asm/WelcomePage.html")

def MedicalSupplies(request):
    medicalSupplies = MedicalSupplies.objects.all()

    context = {
        "medicalSupplies" = medicalSupplies
    }

    return render(request, "asm/MedicalSupplies.html")

def foodSupplies(request):
    foodSupplies = FoodSupplies.objects.all()

    context = {
        "foodSupplies" = foodSupplies
    }

    return render(request, "asm/foodSupplies.html")

def electronicSupplies(request):
    electronicSupplies = ElectronicSupplies.objects.all()

    context = {
        "electronicSupplies" = electronicSupplies
    }

    return render(request, "asm/electronicSupplies.html")

def cleaningSupplies(request):
    cleaningSupplies = CleaningSupplies.objects.all()

    context = {
        "cleaningSupplies" = cleaningSupplies
    }

    return render(request, "asm/cleaningSupplies.html")

 