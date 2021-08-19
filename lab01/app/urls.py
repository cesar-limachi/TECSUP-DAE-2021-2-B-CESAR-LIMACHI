from django.urls import path

from . import views

urlpatterns = [

    ### nos muestra el contenido de las vista index.
    path('', views.index, name='index'),
    ### especificamos la continuacion de la URL app/sumar y ponemos los parametros a sumar
    path('sumar/<int:numero1>/<int:numero2>/',views.sumar,name='suma'),
    ### especificamos la continuacion de la URL app/restar y ponemos los parametros a restar
    path('restar/<int:numero1>/<int:numero2>/',views.restar,name='resta'),
    ### especificamos la continuacion de la URL app/multiplicar y ponemos los parametros a multiplicar
    path('multiplicar/<int:numero1>/<int:numero2>/',views.multiplicar,name='multiplicacion'),
    ### especificamos la continuacion de la URL app/dividir y ponemos los parametros a dividir
    path('dividir/<int:numero1>/<int:numero2>/',views.dividir,name='dividir')

]
