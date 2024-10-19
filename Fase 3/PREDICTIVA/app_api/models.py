from django.db import models

class Coleccion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Data(models.Model):
    coleccion = models.ForeignKey(Coleccion, related_name='data', on_delete=models.CASCADE)
    sensorValue = models.FloatField()
    timestamp = models.IntegerField()

    def __str__(self):
        return f"{self.coleccion.nombre} - {self.timestamp}"

class Usuario(models.Model):
    user = models.CharField(max_length=100, unique=True)
    pass_field = models.IntegerField(default=1234)
    def __str__(self):
        return self.user
    
class Estadisticas(models.Model):
    aperturas = models.IntegerField(default=0)
    def __str__(self):
        return self.aperturas