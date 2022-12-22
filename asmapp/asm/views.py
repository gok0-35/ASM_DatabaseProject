from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def WelcomePage(request):
    return render(request, "asm/WelcomePage.html")

def MedicalSupplies(request):
    return render(request, "asm/MedicalSupplies.html")

def foodSupplies(request):
    return render(request, "asm/foodSupplies.html")

def electronicSupplies(request):
    return render(request, "asm/electronicSupplies.html")

def cleaningSupplies(request):
    return render(request, "asm/cleaningSupplies.html")

def AddSupplies(request):
    return render(request, "asm/AddSupplies.html")    