from django.urls import path
from .views import home_requisitor, home_administrador, home_supervisor, home_tester

app_name = 'restrito'
urlpatterns = [
    path('requisitor', home_requisitor, name='home_requisitor'),
    path('administrador', home_administrador, name='home_administrador'),
    path('supervisor', home_supervisor, name='home_supervisor'),
    path('tester', home_tester, name='home_tester')
]
