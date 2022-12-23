from django.db import models

# Create your models here.
class Users(models.Model):
    nameUsers = models.CharField(max_length=45, default = '')
    surnameUsers = models.CharField(max_length=45, default = '')
    passwordUserss = models.CharField(max_length=45, default = '')
    phoneNumberUsers = models.CharField(max_length=45, default = '')
    emailUsers = models.CharField(max_length=45, default = '')

    def __str__(self):
       return f"{self.nameUsers} {self.surnameUsers}"

class MedicalSupplies(models.Model):
    nameMedicalSupplies = models.CharField(max_length=45)
    priceMedicalSupplies = models.CharField(max_length=45)
    quantityMedicalSupplies = models.IntegerField()
    expirationMedicalSupplies = models.CharField(max_length=45)
    buyDateMedicalSupplies = models.CharField(max_length=45)
    buyerMedicalSupplies = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
       return f"{self.nameMedicalSupplies} {self.quantityMedicalSupplies}"

class ElectronicSupplies(models.Model):
    nameElectronicSupplies = models.CharField(max_length=45)
    priceElectronicSupplies= models.CharField(max_length=45)
    quantityElectronicSupplies = models.IntegerField()
    buyDateElectronicSupplies = models.CharField(max_length=45)
    buyerElectronicSupplies = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
       return f"{self.nameElectronicSupplies} {self.quantityElectronicSupplies}"

class CleaningSupplies(models.Model):
    nameCleaningSupplies = models.CharField(max_length=45)
    priceCleaningSupplies= models.CharField(max_length=45)
    quantityCleaningSupplies = models.IntegerField()
    buyDateCleaningSupplies = models.CharField(max_length=45)
    buyerCleaningSupplies = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
       return f"{self.nameCleaningSupplies} {self.quantityCleaningSupplies}"

class FoodSupplies(models.Model):
    nameFoodSupplies = models.CharField(max_length=45)
    priceFoodSupplies = models.CharField(max_length=45)
    quantityFoodSupplies = models.IntegerField()
    expirationFoodSupplies = models.CharField(max_length=45)
    buyDateFoodSupplies = models.CharField(max_length=45)   
    buyerFoodSupplies = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
       return f"{self.nameFoodSupplies} {self.quantityFoodSupplies}"

