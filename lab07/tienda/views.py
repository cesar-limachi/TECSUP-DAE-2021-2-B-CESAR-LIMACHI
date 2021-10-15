from django.shortcuts import get_object_or_404, render
from .models import Producto, Categoria
# Create your views here.

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categoria = Categoria.objects.all()
    context={
        'product_list':product_list,
        'categoria':categoria
    }
    return render(request,'index.html',context)

def producto(request,producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categoria= Categoria.objects.all()
    return render(request,'producto.html',{'producto':producto,'categoria':categoria})

def categoria(request,categoria_id):
    categoria = Categoria.objects.all()
    producto = Producto.objects.filter(categoria_id=categoria_id)
    return render(request,'categoria.html',{'categoria':categoria,'producto':producto})

from tienda.carrito import Cart

def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')
