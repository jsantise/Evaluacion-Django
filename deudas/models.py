from __future__ import unicode_literals

from django.db import models

EstadoCivil = (  
    ('SOL', 'SOLTERO'),
    ('CAS', 'CASADO'),
    ('VIU', 'VIUDO'),
    ('DIV', 'DIVORCIADO'),
)



class Deudor(models.Model):
    rut = models.CharField(max_length=20)
    nombres = models.CharField(max_length=200)
    apellidoPaterno = models.CharField(max_length=200)
    apellidoMaterno = models.CharField(max_length=200)
    estadoCivil = models.CharField(max_length=3, choices=EstadoCivil)
    fechaDeNacimiento = models.DateField()

    def __str__(self):
        return self.rut

class Deuda(models.Model):
    deudor = models.ForeignKey(Deudor, on_delete=models.CASCADE)
    fechaDeInicioDeuda = models.DateField()
    montoDeuda = models.IntegerField(default=0)
    acreedor = models.CharField(max_length=200)
    def __str__(self):
        return self.acreedor

