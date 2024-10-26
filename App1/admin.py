from django.contrib import admin
from App1.models import Vehiculo

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['marca', 'patente', 'modelo', 'color', 'tipo']

admin.site.register(Vehiculo, VehiculoAdmin)