# Generated by Django 3.2.9 on 2022-12-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asm', '0004_auto_20221223_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='emailUsers',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='users',
            name='nameUsers',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='users',
            name='passwordUserss',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='users',
            name='phoneNumberUsers',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='users',
            name='surnameUsers',
            field=models.CharField(default='', max_length=45),
        ),
    ]
