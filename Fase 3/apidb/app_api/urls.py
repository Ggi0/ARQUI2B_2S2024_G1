# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ColeccionViewSet, DataViewSet

router = DefaultRouter()
router.register(r'colecciones', ColeccionViewSet)
router.register(r'data', DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]