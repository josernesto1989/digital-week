from django.db import models


class Tecnico(models.Model):
    nombre = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.nombre

class TipoTrabajo(models.Model):
    nombre = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.nombre
class Semana(models.Model):
    nombre = models.CharField(max_length=255)
    abierta = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.nombre}'   
class Dia(models.Model):
    fecha = models.DateField()
    sobrante = models.IntegerField(null=True)
    semana = models.ForeignKey(Semana,on_delete=models.CASCADE, related_name='dias')
    abierto = models.BooleanField(default=False)
    def __str__(self):
        return str(self.fecha)
class OtroGasto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    comentarios = models.CharField(max_length=255,null=True, blank=True)
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE,related_name='otrosGastos')
    def __str__(self):
        return f'{self.nombre} - {self.precio}'

class PiezaAPagar(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    comentarios = models.CharField(max_length=255,null=True, blank=True)
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='piezasAPagar')
    
    def __str__(self):
        return self.nombre
class Venta(models.Model):
    nombre = models.CharField(max_length=255)
    hora = models.TimeField()
    ingreso = models.IntegerField(null=True, blank=True)
    costo = models.IntegerField(null=True, blank=True)
    tecnico = models.ForeignKey(Tecnico,on_delete=models.CASCADE, related_name='ventas')
    tipoTrabajo = models.ForeignKey(TipoTrabajo,on_delete=models.CASCADE, related_name='ventas')
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='ventas')
    
    def __str__(self):
        return f'{self.tipoTrabajo} {self.nombre} {self.ingreso}'
    
# Create your models here.