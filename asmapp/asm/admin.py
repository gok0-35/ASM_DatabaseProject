from django.contrib import admin
from .models import Users
from .models import MedicalSupplies
from .models import ElectronicSupplies
from .models import FoodSupplies
from .models import CleaningSupplies

# Register your models here.
admin.site.register(Users)
admin.site.register(MedicalSupplies)
admin.site.register(ElectronicSupplies)
admin.site.register(FoodSupplies)
admin.site.register(CleaningSupplies)