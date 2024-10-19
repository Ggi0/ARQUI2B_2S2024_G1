# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ColeccionViewSet, DataViewSet, Prediccion, CrearEstadistica, IncrementarAperturas, CrearUsuario, ValidarUsuario

router = DefaultRouter()
router.register(r'colecciones', ColeccionViewSet)
router.register(r'data', DataViewSet)


urlpatterns = [
    path('Prediccion',                      Prediccion.as_view()),
    path('crear-estadistica',               CrearEstadistica.as_view(), name='crear_estadistica'),
    path('incrementar-aperturas/<int:pk>',  IncrementarAperturas.as_view(), name='incrementar_aperturas'),
    path('crear-usuario',                   CrearUsuario.as_view(), name='crear_usuario'),
    path('validar-usuario',                 ValidarUsuario.as_view(), name='validar_usuario'),
    # Url genericas para las colecciones y data
    path('', include(router.urls)),
]