# Generated by Django 3.2.9 on 2022-12-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CleaningSupplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCleaningSupplies', models.CharField(max_length=45)),
                ('typeCleaningSupplies', models.CharField(max_length=45)),
                ('priceCleaningSupplies', models.CharField(max_length=45)),
                ('quantityCleaningSupplies', models.CharField(max_length=45)),
                ('expirationCleaningSupplies', models.CharField(max_length=45)),
                ('buyDateCleaningSupplies', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ElectronicSupplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameElectronicSupplies', models.CharField(max_length=45)),
                ('typeElectronicSupplies', models.CharField(max_length=45)),
                ('priceElectronicSupplies', models.CharField(max_length=45)),
                ('quantityElectronicSupplies', models.CharField(max_length=45)),
                ('expirationElectronicSupplies', models.CharField(max_length=45)),
                ('buyDateElectronicSupplies', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='FoodSupplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameFoodSupplies', models.CharField(max_length=45)),
                ('typeFoodSupplies', models.CharField(max_length=45)),
                ('priceFoodSupplies', models.CharField(max_length=45)),
                ('quantityFoodSupplies', models.CharField(max_length=45)),
                ('expirationFoodSupplies', models.CharField(max_length=45)),
                ('buyDateFoodSupplies', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalSupplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameMedicalSupplies', models.CharField(max_length=45)),
                ('typeMedicalSupplies', models.CharField(max_length=45)),
                ('priceMedicalSupplies', models.CharField(max_length=45)),
                ('quantityMedicalSupplies', models.CharField(max_length=45)),
                ('expirationMedicalSupplies', models.CharField(max_length=45)),
                ('buyDateMedicalSupplies', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameUsers', models.CharField(max_length=45)),
                ('surnameUsers', models.CharField(max_length=45)),
                ('PasswordUsers', models.CharField(max_length=45)),
                ('PhoneNumberUsers', models.CharField(max_length=45)),
            ],
        ),
    ]
