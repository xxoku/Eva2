from django.shortcuts import render, redirect
from App1.forms import FormVehiculo
from App1.models import Vehiculo

# Create your views here.

def index (request):
    return render (request, 'index.html')

def listadoVehiculos(request):
    vehiculos = Vehiculo.objects.all()
    data = {'vehiculos': vehiculos}
    return render(request, 'vehiculos.html', data)

def agregarVehiculo(request):
    form = FormVehiculo()
    if request.method == 'POST' :
        form = FormVehiculo(request.POST)
        if form.is_valid() : 
            form.save()
        return redirect('/vehiculos')
    data = {'form' : form}
    return render(request, 'agregarVehiculo.html', data)

def eliminarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(id = id)
    vehiculo.delete()
    return redirect ('/vehiculos')

def actualizarVehiculos(request, id): 
    vehiculo = Vehiculo.objects.get(id = id)
    form = FormVehiculo(instance=vehiculo)
    if request.method == 'POST' : 
        form = FormVehiculo(request.POST, instance=vehiculo)
        if form.is_valid() : 
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarVehiculo.html', data)
