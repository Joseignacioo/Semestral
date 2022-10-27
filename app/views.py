from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

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
