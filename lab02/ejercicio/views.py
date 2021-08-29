import math
from django.shortcuts import render
from math import *

# Create your views here.

def index(request):
    context = {
        'titulo':'Formulario',
    }
    return render(request, 'ejercicio/form.html', context)

def enviar(request):

    numero1 = int(request.POST['num1'])
    numero2 = int(request.POST['num2']) 
    operacion = request.POST['operacion']
    respuesta = 0

    if operacion == 'suma':
        respuesta = numero1 + numero2
    elif operacion == 'resta':
        respuesta = numero1 - numero2
    elif operacion == 'multiplicacion':
        respuesta = numero1 * numero2
    elif operacion == 'division':
        respuesta = numero1 / numero2
    
    context = {
        'titulo' : "Respuesta",
        'num1' : numero1,
        'num2' : numero2,
        'resultado' : '{:.2f}'.format(respuesta),
        'operacion' : operacion,   
    }

    return render(request, 'ejercicio/respu.html', context)


def Cilindro(request):
    context = {
        'titulo' : "CALCULAR EL VOLUMEN DEL CILINDRO"
    }
    return render(request, 'ejercicio/cilindro.html', context)

def enviarCilindro(request):
    altura = int(request.POST['altura'])
    diametro = int(request.POST['diametro'])
    respuesta = pi * math.pow(diametro/2, 2) * altura
    context = {
        'respuesta' : '{:.2f}'.format(respuesta)
    }
    return render(request, 'ejercicio/resultadoCilindro.html', context)