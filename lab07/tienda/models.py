from django.db import models
from django.db.models.base import Model

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos', blank=True,null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=9)
    email = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateTimeField('fecha de nacimiento')
    fecha_publicacion = models.DateTimeField('fecha de publicacion')

    def __str__(self):
        return self.nombre