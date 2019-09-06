"""gerenciador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from placas import urls
from testes import urls
from requisicao import urls
from restrito import urls
from indicadores import urls
from core import urls

urlpatterns = [
    path('', include('core.urls')),
    path('', include('requisicao.urls')),
    path('placas/', include('placas.urls')),
    path('testes/', include('testes.urls')),
    path('restrito/', include('restrito.urls')),
    path('dashboard/', include('indicadores.urls')),
    path('admin/', admin.site.urls)
   

]
