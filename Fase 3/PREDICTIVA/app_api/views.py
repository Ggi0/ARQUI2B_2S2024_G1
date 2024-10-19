from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Coleccion, Data, Usuario, Estadisticas
from .serializers import ColeccionSerializer, DataSerializer, UsuarioSerializer, EstadisticasSerializer
from django.contrib.auth.hashers import make_password, check_password
from red_neuronal import solicitar_prediccion
from django.http import HttpResponse, JsonResponse

class ColeccionViewSet(viewsets.ModelViewSet):
    queryset = Coleccion.objects.all()
    serializer_class = ColeccionSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class Prediccion(generics.GenericAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    def get(self, request, *args, **kwargs):
        fecha_timestamp = request.GET.get('fecha_timestamp', '')
        id_coleccion    = request.GET.get('id_coleccion', '')
        mensaje, prediccion = solicitar_prediccion(id_coleccion, fecha_timestamp)
        data = {
            'status' : prediccion > 0,
            'resultado' : prediccion,
            'mensaje': mensaje
        }
        return JsonResponse(data)

class CrearEstadistica(generics.CreateAPIView):
    queryset = Estadisticas.objects.all()
    serializer_class = EstadisticasSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Estadística creada", "id": serializer.data['id']}, 
                        status=status.HTTP_201_CREATED, headers=headers)

class IncrementarAperturas(generics.UpdateAPIView):
    queryset = Estadisticas.objects.all()
    serializer_class = EstadisticasSerializer
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"message": "Consulta exitosa", "aperturas": serializer.data['aperturas']})
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.aperturas += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response({"message": "Aperturas incrementadas", "aperturas": serializer.data['aperturas']})

class CrearUsuario(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Usuario creado", "id": serializer.data['id']}, 
                        status=status.HTTP_201_CREATED, headers=headers)

class ValidarUsuario(generics.GenericAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        user = request.data.get('user')
        password = request.data.get('password')
        
        if not user or not password:
            return Response({"message": "Se requieren usuario y contraseña", 'ok': False}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        try:
            usuario = Usuario.objects.get(user=user)
        except Usuario.DoesNotExist:
            return Response({"message": "Usuario no encontrado", 'ok': False}, 
                            status=status.HTTP_404_NOT_FOUND)
        
        
        if int(password) == int(usuario.pass_field):
            return Response({"message": "Usuario validado correctamente", 'ok': True}, 
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": "Contraseña incorrecta", 'ok': False}, 
                            status=status.HTTP_401_UNAUTHORIZED)
