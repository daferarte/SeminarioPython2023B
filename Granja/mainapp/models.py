from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre documento')
    descripcion = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripcion')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='actualizado')
    
    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'
    
    def __str__(self):
        return str(self.nombre)

class Personas(models.Model):
    tipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, verbose_name='Tipo de documento', blank=True, null=True)
    usuario = models.OneToOneField(User, verbose_name='Usuario', blank=True, null=True, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=12, unique=True, verbose_name='Cedula')
    direccion = models.CharField(max_length=150, verbose_name='Direccion')
    fNacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de cumpleaños')
    telefono = models.CharField(max_length=10, null=True, blank=True, verbose_name='Telefono')
    imagen = models.ImageField(default='null', verbose_name='Imagen', upload_to='usuario', blank=True, null=True)
    publicado = models.BooleanField(default=False, verbose_name='Publicado?')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='actualizado')
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        
    
    def __str__(self):
        return str(self.cedula)