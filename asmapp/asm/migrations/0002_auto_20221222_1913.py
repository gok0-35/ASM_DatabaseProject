# Generated by Django 3.2.9 on 2022-12-22 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaningsupplies',
            name='buyerCleaningSupplies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asm.users'),
        ),
        migrations.AddField(
            model_name='electronicsupplies',
            name='buyerElectronicSupplies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asm.users'),
        ),
        migrations.AddField(
            model_name='foodsupplies',
            name='buyerFoodSupplies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asm.users'),
        ),
        migrations.AddField(
            model_name='medicalsupplies',
            name='buyerMedicalSupplies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asm.users'),
        ),
        migrations.AlterField(
            model_name='cleaningsupplies',
            name='quantityCleaningSupplies',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='electronicsupplies',
            name='quantityElectronicSupplies',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='foodsupplies',
            name='quantityFoodSupplies',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='medicalsupplies',
            name='quantityMedicalSupplies',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='PhoneNumberUsers',
            field=models.IntegerField(),
        ),
    ]