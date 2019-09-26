from django.urls import path
from placas import views

app_name = 'placas' 

urlpatterns = [
    #Urls modelo
    path('lista-modelo/', views.lista_modelo, name="lista-modelo"),
    path('cadastrar-modelo/', views.cadastrar_modelo, name="cadastrar-modelo"),
    path('excluir-modelo/<int:id>', views.excluir_modelo, name="excluir-modelo"),
    path('atualiza-modelo/<int:id>', views.atualiza_modelo, name="atualiza-modelo"),

    #Urls placa
    path('lista-placa/', views.lista_placa, name="lista-placa"),
    path('cadastrar-placa/', views.cadastrar_placa, name="cadastrar-placa"  ),
    path('cadastrar-lote/', views.cadastrar_lote, name="cadastrar-lote"),
    path('excluir-placa/<int:id>', views.excluir_placa, name="excluir-placa" ),
    path('atualiza-placa/<int:id>', views.atualiza_placa, name="atualiza-placa")
    
    
    ]