from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recolector

# Create your views here.

def agregar(request):
    
    if request.method == 'POST':
        
        cedula=request.POST.get('cedula')
        nombres=request.POST.get('nombres')
        apellidos=request.POST.get('apellidos')
        direccion=request.POST.get('direccion')
        fecnac=request.POST.get('fecnac')
        telefono=request.POST.get('telefono')
        
        miRecolector=Recolector.objects.create(
            cedula=cedula, 
            nombres=nombres,
            apellido=apellidos,
            direccion=direccion,
            fNacimiento=fecnac,
            telefono=telefono
        )
        
        messages.success(request, 'Registrado correctamente')
        return redirect('/')
        
    return render(request, 'recolector/agregar.html',{
        'title': 'Agregar recolector',
    })
    
def mostrar(request):
    recolectores=Recolector.objects.all()
    return render(request, 'recolector/mostrar.html',{
        'title': 'Recolectores',
        'recolectores': recolectores
    })