# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
from django.contrib import admin
from .models import CarMake, CarModel

# Registering CarMake
admin.site.register(CarMake)

# Registering CarModel
admin.site.register(CarModel)
