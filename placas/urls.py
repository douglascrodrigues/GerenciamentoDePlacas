from django.urls import path
from placas import views

app_name = 'placas' 

urlpatterns = [
    path('cadastrar-modelo/', views.cadastrar_modelo, name="cadastrar-modelo"),
    path('cadastrar-placa/', views.cadastrar_placa, name="cadastrar-placa")
    
    ]