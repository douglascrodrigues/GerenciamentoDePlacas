from django.urls import path
from testes import views

app_name = 'testes' 

urlpatterns = [
    path('<str:caminho>/', views.testes, name="testes1")
    
    ]