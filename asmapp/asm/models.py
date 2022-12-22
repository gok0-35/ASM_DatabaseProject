from django.db import models

# Create your models here.
class Users(models.Model):
    nameUsers = models.CharField(max_length=45)
    surnameUsers = models.CharField(max_length=45)
    PasswordUsers = models.CharField(max_length=45)
    PhoneNumberUsers = models.CharField(max_length=45)

class MedicalSupplies(models.Model):
    nameMedicalSupplies = models.CharField(max_length=45)
    typeMedicalSupplies = models.CharField(max_length=45)
    priceMedicalSupplies = models.CharField(max_length=45)
    quantityMedicalSupplies = models.IntegerField()
    expirationMedicalSupplies = models.CharField(max_length=45)
    buyDateMedicalSupplies = models.CharField(max_length=45)
    buyerMedicalSupplies = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

class ElectronicSupplies(models.Model):
    nameElectronicSupplies = models.CharField(max_length=45)
    typeElectronicSupplies = models.CharField(max_length=45)
    priceElectronicSupplies= models.CharField(max_length=45)
    quantityElectronicSupplies = models.IntegerField()
    expirationElectronicSupplies = models.CharField(max_length=45)
    buyDateElectronicSupplies = models.CharField(max_length=45)
    buyerElectronicSupplies = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

class CleaningSupplies(models.Model):
    nameCleaningSupplies = models.CharField(max_length=45)
    typeCleaningSupplies = models.CharField(max_length=45)
    priceCleaningSupplies= models.CharField(max_length=45)
    quantityCleaningSupplies = models.IntegerField()
    expirationCleaningSupplies = models.CharField(max_length=45)
    buyDateCleaningSupplies = models.CharField(max_length=45)
    buyerCleaningSupplies = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

class FoodSupplies(models.Model):
    nameFoodSupplies = models.CharField(max_length=45)
    typeFoodSupplies = models.CharField(max_length=45)
    priceFoodSupplies = models.CharField(max_length=45)
    quantityFoodSupplies = models.IntegerField()
    expirationFoodSupplies = models.CharField(max_length=45)
    buyDateFoodSupplies = models.CharField(max_length=45)   
    buyerFoodSupplies = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)