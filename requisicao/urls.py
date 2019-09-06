from django.urls import path
from requisicao import views

app_name = 'requisicao'

urlpatterns = [
    path('requisicao/', views.requisicao, name="requisicao1")
    
    ]