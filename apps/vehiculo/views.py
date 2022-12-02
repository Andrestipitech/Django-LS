from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.vehiculo.forms import VehiculoForm
from apps.vehiculo.models import Vehiculo 

def vehiculo_view(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehiculo:lista')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/crear_vehiculo.html', {'form': form})