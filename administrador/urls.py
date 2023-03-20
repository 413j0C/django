from django.urls import path
from administrador.views import activosTotales, loginPanel

urlpatterns = [
    path('login/dashboard',activosTotales, name='dashboard'),
]
