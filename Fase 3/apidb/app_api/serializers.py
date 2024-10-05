# serializers.py
from rest_framework import serializers
from .models import Coleccion, Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id', 'coleccion', 'sensorValue', 'timestamp']

class ColeccionSerializer(serializers.ModelSerializer):
    data = DataSerializer(many=True, read_only=True)

    class Meta:
        model = Coleccion
        fields = ['id', 'nombre', 'data']
