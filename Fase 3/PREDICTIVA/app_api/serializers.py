# serializers.py
from rest_framework import serializers
from .models import Coleccion, Data, Usuario, Estadisticas

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id', 'coleccion', 'sensorValue', 'timestamp']

class ColeccionSerializer(serializers.ModelSerializer):
    data = DataSerializer(many=True, read_only=True)

    class Meta:
        model = Coleccion
        fields = ['id', 'nombre', 'data']

# Serializers
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'user', 'pass_field']
        extra_kwargs = {'pass_field': {'write_only': True}}

class EstadisticasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadisticas
        fields = ['id', 'aperturas']