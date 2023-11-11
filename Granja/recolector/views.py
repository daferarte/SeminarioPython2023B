from django.shortcuts import render, redirect, get_object_or_404
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
    
def editar(request, pk):
    
    if request.method == 'POST':
        
        cedula=request.POST.get('cedula')
        nombres=request.POST.get('nombres')
        apellidos=request.POST.get('apellidos')
        direccion=request.POST.get('direccion')
        fecnac=request.POST.get('fecnac')
        telefono=request.POST.get('telefono')
        
        miRecolector=Recolector.objects.filter(pk=pk).update(
            cedula=cedula, 
            nombres=nombres,
            apellido=apellidos,
            direccion=direccion,
            fNacimiento=fecnac,
            telefono=telefono
        )
        
        messages.success(request, 'Actualizado correctamente')
        return redirect('mostrar_recolector')
    
    recolector = Recolector.objects.get(pk=pk)
    
    return render(request, 'recolector/editar.html',{
        'title': 'Recolectores',
        'recolector': recolector
    })
    
def eliminar(request, pk):
    recolector= get_object_or_404(Recolector, pk=pk)
    recolector.delete()
    messages.success(request, 'Borrado correctamente')
    return redirect('mostrar_recolector')