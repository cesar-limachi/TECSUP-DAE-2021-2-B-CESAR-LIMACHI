from django.urls import path

from . import views

app_name = 'ejercicio'

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
    path('cilindro',views.Cilindro,name='indexCilindro'),
    path('enviar/cilindro',views.enviarCilindro,name='enviarCilindro'),
]