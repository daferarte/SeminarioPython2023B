from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Recolector
# aqui se importan librerias de api de django
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .serializers import RecolectorSerializer

# CRUD de django modelo por metodos tradicional

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

# modelo de django por clases para API

class Recolector_APIView_List(APIView):
    def get(self, request, format=None, *args, **kwargs):
        recolectores=Recolector.objects.all()
        serializer=RecolectorSerializer(recolectores, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print(request.data.get('credential'))
        serializer=RecolectorSerializer(data=request.data.get('credential'))
        
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Recolector_APIView_Detail(APIView):
    
    def get_object(self, pk):
        try:
            return Recolector.objects.get(pk=pk)
        except Recolector.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        recolector = self.get_object(pk)
        serializer = RecolectorSerializer(recolector)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        recolector = self.get_object(pk)
        serializer = RecolectorSerializer(recolector, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        recolector = self.get_object(pk)
        recolector.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)