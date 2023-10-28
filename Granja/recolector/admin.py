from django.contrib import admin
from .models import Recolector

# Register your models here.

class RecolectorAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombres','apellido','creado','actualizado')
    readonly_fields =('creado', 'actualizado')
    search_fields=('cedula', 'nombres', 'apellido')
    list_filter=('cedula', 'nombres', 'apellido')
    ordering=('-creado',)

admin.site.register(Recolector, RecolectorAdmin)
