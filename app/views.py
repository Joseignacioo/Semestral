from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


''' PRODUCTOS '''
def productos(request):
    productos =  Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)

@permission_required('app.view_producto')
@permission_required('app.add_producto')
def adminStock(request):
    productos = Producto.objects.all()
    data= {
        'form' : ProductoForm(),
        'productos': productos
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():   
            formulario.save()
            data["mensaje"] = "guardado correctamente"
            return redirect("adminStock")
        else:
            data['form'] = formulario
        
    return render(request, 'app/admin/stock.html', data)
@permission_required('app.change_producto')
def adminModificarProducto(request,id):
    productos = get_object_or_404(Producto, id=id)
    data= {
        'form': ProductoForm(instance=productos)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():   
            formulario.save()
            data["mensaje"] = "guardado correctamente"
            return redirect("adminStock")
        else:
            data['form'] = formulario
        
    return render(request, 'app/admin/stock/modificar.html', data)
@permission_required('app.delete_producto')
def adminEliminarProductos(request, id):
    productos = get_object_or_404(Producto, id=id)
    productos.delete()
    return redirect("adminStock")
    
''' END PRODUCTOS '''

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():   
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect("home")
        else:
            data['form'] = formulario
    return render(request, 'registration/registro.html',data)


def recetaMedica(request):
    return render(request, 'app/receta-medica.html')

def adminVentas(request):
    return render(request, 'app/admin/ventas.html')













def adminSolicitudStock(request):
    return render(request, 'app/admin/solicitud-stock.html')

def adminEstadoStock(request):
    return render(request, 'app/admin/estado-stock.html')

def adminInformeRecetas(request):
    return render(request, 'app/admin/informe-recetas.html')

def adminSolicitudLaboratorio(request):
    return render(request, 'app/admin/solicitud-laboratorio.html')

def adminEstadoLaboratorio(request):
    return render(request, 'app/admin/estado-laboratorio.html')
