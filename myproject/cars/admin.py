from django.contrib import admin

from .models import Car, Driver
# Register your models here.

admin.site.register(Driver)
admin.site.register(Car)