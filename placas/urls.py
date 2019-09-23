from django.urls import path
from placas import views

app_name = 'placas' 

urlpatterns = [
    path('cadastrar-modelo/', views.cadastrar_modelo, name="cadastrar-modelo"),
    path('lista-placa/', views.lista_placa, name="lista-placa"),
    path('cadastrar-placa/', views.cadastrar_placa, name="cadastrar-placa"  ),
    path('excluir-placa/<int:id>', views.excluir_placa, name="excluir-placa" ),
    path('atualiza-placa/<int:id>', views.atualiza_placa, name="atualiza-placa")
    
    ]