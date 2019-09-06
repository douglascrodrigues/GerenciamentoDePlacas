from django.urls import path, include
from django.contrib import admin
from core import views



app_name = 'core'

urlpatterns = [
    
    path('', views.home, name="home"),
    path('entrar', views.entrar, name="entrar"),
    path('sair', views.sair, name="sair"), 

    ]