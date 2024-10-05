from django.db import models

# models.py
from django.db import models

class Coleccion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Data(models.Model):
    coleccion = models.ForeignKey(Coleccion, related_name='data', on_delete=models.CASCADE)
    sensorValue = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return f"{self.coleccion.nombre} - {self.timestamp}"

