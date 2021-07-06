from .models import Cart, CartDetail, Category, Product
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .forms import FormProduct
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# Create your views here.
def index(request):
    return render( request, 'index.html', {
        "lista_categorias" : Category.objects.all() ,
        "lista_ultimos_productos" : Product.objects.order_by('created_at').reverse()[:3],
        "lista_mas_productos" : Product.objects.order_by('created_at').reverse()[3:],

    })
    
def acerca_de(request):
    return render( request, 'acercade.html',{
        "lista_categorias" : Category.objects.all()
    })

def categoria(request,id):
    return render( request, 'productos.html',{
        "lista_productos" : Product.objects.filter(category_id=id).order_by('created_at').reverse(),
        "lista_categorias" : Category.objects.all()
    })

def buscar(request):
    texto = request.GET.get('texto')
    lista_productos = None
    if texto is None or len(texto.strip()) == 0:
        lista_productos = Product.objects.all().order_by('created_at').reverse()
    else:
        lista_productos = Product.objects.filter(Q(title__contains=texto) | Q(description__contains=texto)).order_by('created_at').reverse()
    return render( request, 'productos.html',{
        "lista_productos" : lista_productos,
        "lista_categorias" : Category.objects.all()
    })

def productos(request):
    return render( request, 'productos.html',{
        "lista_productos" : Product.objects.order_by('created_at').reverse(),
        "lista_categorias" : Category.objects.all()
    })

@permission_required('WEBSITE.add_product')
def producto_nuevo(request):
    if request.method == "POST":
        form = FormProduct( request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render( request, 'productos.html',{
                "lista_productos" : Product.objects.all().order_by('created_at').reverse(),
                "lista_categorias" : Category.objects.all()
            })
    else:
        form = FormProduct()
        return render( request, 'producto_nuevo.html',{
            "lista_categorias" : Category.objects.all(),
            "form" : form
        })

def producto(request, id):
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name='moderador').exists():
            return HttpResponseRedirect(reverse("producto_editar", args=(id,)))
        else:
            return render( request, 'producto.html',{
                "producto" : Product.objects.get(pk=id),
                "lista_categorias" : Category.objects.all()
            })
    else:
        return render( request, 'producto.html',{
            "producto" : Product.objects.get(pk=id),
            "lista_categorias" : Category.objects.all()
        })

@permission_required('WEBSITE.change_product')
def producto_editar(request, id):
    producto = Product.objects.get(pk=id)
    if request.method == "POST":
        form = FormProduct( request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return render( request, 'productos.html',{
                "lista_productos" : Product.objects.all().order_by('created_at').reverse(),
                "lista_categorias" : Category.objects.all()
            })
    else:
        form = FormProduct( instance=producto)
        return render( request, 'producto_editar.html',{
            "producto": producto,
            "form": form,
            "lista_categorias" : Category.objects.all()
        })

def producto_borrar(request, id):
    producto = get_object_or_404(Product, id=id)
    producto.delete()
    return render( request, 'productos.html',{
                "lista_productos" : Product.objects.all().order_by('created_at').reverse(),
                "lista_categorias" : Category.objects.all()
            })

@login_required
def agregar_al_carrito(request, id):
    producto = get_object_or_404(Product, id=id)
    user = request.user
    num_carrito = Cart.objects.filter(user=user).count()
    if num_carrito == 0:
        carrito = Cart(user=user, total=0)
        carrito.save()

    carrito = Cart.objects.get(user=user)
    carrito_detalle = CartDetail(cart=carrito, product=producto, quantity= 1, price= producto.price, total= producto.price)
    carrito_detalle.save()
    contador = CartDetail.objects.filter(cart=carrito.id).count()
    request.session['contador'] = contador
    return HttpResponseRedirect(reverse("index"))

@login_required
def ver_carrito(request):
    user = request.user
    if user.groups.filter(name='moderador').exists():
        return HttpResponseRedirect(reverse("index"))

    carrito = Cart.objects.get(user=user)
    carrito_detalle = CartDetail.objects.filter(cart=carrito.id)
    return render( request, 'ver_carrito.html', {
        "items_carrito": carrito_detalle, 
        "lista_categorias" : Category.objects.all()
    })

@login_required
def eliminar_item_carrito(request, id):
    item_carrito = get_object_or_404(CartDetail, id=id)
    item_carrito.delete();
    user = request.user
    carrito = Cart.objects.get(user=user)
    contador = CartDetail.objects.filter(cart=carrito.id).count()
    request.session['contador'] = contador
    return HttpResponseRedirect(reverse("ver_carrito"))

@login_required
def vaciar_carrito(request):
    user = request.user
    carrito = Cart.objects.get(user=user)
    items = CartDetail.objects.filter(cart=carrito.id)
    items.delete()
    contador = CartDetail.objects.filter(cart=carrito.id).count()
    request.session['contador'] = contador
    return HttpResponseRedirect(reverse("ver_carrito"))


