from django.db import models


class Tecnico(models.Model):
    nombre = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.nombre

class TipoTrabajo(models.Model):
    nombre = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.nombre
    
    
class OtrosGastos(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    comentarios = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.nombre} - {self.precio}'

class PiezasAPagar(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    comentarios = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Dia(models.Model):
    fecha = models.DateField()
    sobrante = models.IntegerField()
    #TODO: incomplete
class Venta(models.Model):
    nombre = models.CharField(max_length=255)
    hora = models.TimeField()
    ingreso = models.IntegerField()
    costo = models.IntegerField()
    tecnico = models.ForeignKey(Tecnico)
    tipoTrabajo = models.ForeignKey(TipoTrabajo)
    
    def __str__(self):
        return f'{self.tipoTrabajo} {self.nombre} {self.ingreso}'
    
# Create your models here.