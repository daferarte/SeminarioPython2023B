from django.contrib import admin
from .models import TipoDocumento, Personas

# Register your models here.
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre','creado','actualizado')
    readonly_fields =('creado', 'actualizado')
    search_fields=('nombre',)
    ordering=('-creado',)
    
class PersonasAdmin(admin.ModelAdmin):
    list_display = ('usuario','cedula','direccion','fNacimiento','telefono','creado','actualizado')
    readonly_fields =('creado', 'actualizado')
    search_fields=('cedula', 'direccion', 'telefono')
    ordering=('-creado',)

    # def save_model(self, request, obj, form, change):
    #     if not obj.user_id:
    #         obj.user_id = request.user.id
    #     obj.save()
    
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Personas, PersonasAdmin)