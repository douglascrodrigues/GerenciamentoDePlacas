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
    path('excluir-placa/<int:id>', views.excluir_placa, name="excluir-placa" ),
    path('atualiza-placa/<int:id>', views.atualiza_placa, name="atualiza-placa"),

    #Urls lote
    path('lista-lote/', views.lista_lote, name="lista-lote"),
    path('cadastrar-lote/', views.cadastrar_lote, name="cadastrar-lote"),
    path('excluir-lote/<int:id>', views.excluir_lote, name="excluir-lote"),
    path('atualiza-lote/<int:id>', views.atualiza_lote, name="atualiza-lote")
    
    
    ]