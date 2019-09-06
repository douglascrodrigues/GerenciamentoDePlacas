from django.urls import path
from indicadores import views

app_name = 'indicadores'
urlpatterns = [
    path('<str:caminho>/', views.indicadores, name="indicadores1")
]

