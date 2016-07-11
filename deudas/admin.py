from django.contrib import admin
from deudas.models import Deuda, Deudor


class DeudaAdmin(admin.ModelAdmin):
    list_display = ('deudor','fechaDeInicioDeuda','montoDeuda','acreedor')    

class DeudorAdmin(admin.ModelAdmin):
    list_display = ('rut','nombres','apellidoPaterno','apellidoMaterno','estadoCivil','fechaDeNacimiento')

admin.site.register(Deuda, DeudaAdmin)
admin.site.register(Deudor, DeudorAdmin)
