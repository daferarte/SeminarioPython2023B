from django.db import models

# Create your models here.
class Recolector(models.Model):
    cedula = models.CharField(max_length=12, unique=True, verbose_name='Cedula')
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')
    direccion = models.CharField(max_length=150, verbose_name='Direccion')
    fNacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de cumpleaños')
    telefono = models.CharField(max_length=10, null=True, blank=True, verbose_name='Telefono')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='actualizado')
    
    class Meta:
        verbose_name = 'Recolector'
        verbose_name_plural = 'Recolectores'
        
    def __str__(self):
        return str(self.nombres +' '+ self.apellido)
    
    def calcular_edad(self):
        return date.today().year - self.fNacimiento.year
    
    