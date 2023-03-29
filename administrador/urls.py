from django.urls import path
from administrador.views import activosTotales,formatoPdf

urlpatterns = [
    path('login/dashboard',activosTotales, name='dashboard'),
    path('login/registropdf',formatoPdf,name="registropdf")
]
