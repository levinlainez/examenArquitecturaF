from django.urls import path
from .views import calcular_binarios

urlpatterns = [
    path('calcular/', calcular_binarios, name='calcular_binarios'),
]
