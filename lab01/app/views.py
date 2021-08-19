from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Desde la vista App")

def sumar(request, numero1, numero2):
    sum = numero1 + numero2
    return HttpResponse("La suma de %s + %s = %s" % (numero1, numero2, sum))  
    
    ### !! %s = sicnifica que sera de tipo string !! %f = sera de tipo flotante

def restar(request, numero1, numero2):
    res = numero1 - numero2
    return HttpResponse("La resta de %s - %s = %s" % (numero1, numero2, res))

    ### !! %s = sicnifica que sera de tipo string !! %f = sera de tipo flotante

def multiplicar(request, numero1, numero2):
    mul = numero1 * numero2
    return HttpResponse("La multiplicacion de %s * %s = %s" % (numero1, numero2, mul))

    ### !! %s = sicnifica que sera de tipo string !! %f = sera de tipo flotante

def dividir(request, numero1, numero2):
    div = numero1 / numero2
    return HttpResponse("La division de %s / %s = %f" % (numero1, numero2, div))

    ### !! %s = sicnifica que sera de tipo string !! %f = sera de tipo flotante


