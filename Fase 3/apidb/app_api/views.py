from django.shortcuts import render
from rest_framework import viewsets
from .models import Coleccion, Data
from .serializers import ColeccionSerializer, DataSerializer

class ColeccionViewSet(viewsets.ModelViewSet):
    queryset = Coleccion.objects.all()
    serializer_class = ColeccionSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

