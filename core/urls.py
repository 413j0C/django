"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, salir, formato
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('admin/', admin.site.urls),
    path('',auth_views.LoginView.as_view(),name='inicio'),
    path('', include('django.contrib.auth.urls')),
    path('reiniciar/',auth_views.PasswordResetView.as_view(),name='pass_reset'),
    path('reiniciar/enviar',auth_views.PasswordResetDoneView.as_view(),name='pass_reset_done'),
    path('reiniciar/<uid64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='pass_reset_confirm'),
    path('reiniciar/completo',auth_views.PasswordResetCompleteView.as_view(),name='pass_reset_reset_complete'),
    path('index/', index, name='index'),
    path('formato/', formato, name='formato'),
    path("salir/", salir, name='salir'),
    path('usuarios/',include('usuarios.urls')),
    path('activos/',include('activos.urls')),
    path('activo/',include('activo.urls')),
    path('administrador/',include('administrador.urls')),
]