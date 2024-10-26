from django import forms
from App1.models import Vehiculo

class FormVehiculo(forms.ModelForm):
    class Meta:
        model = Vehiculo 
        fields = '__all__'