from django.urls import path
from administrador.views import activosTotales

urlpatterns = [
    path('login/dashboard',activosTotales, name='dashboard'),
]
