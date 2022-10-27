from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('recetaMedica/',recetaMedica,name="recetaMedica"),
    path('ventas/',adminVentas,name="adminVentas"),
    path('solicitud-stock/',adminSolicitudStock,name="adminSolicitudStock"),
    path('estado-stock/',adminEstadoStock,name="adminEstadoStock"),
    path('informe-recetas/',adminInformeRecetas,name="adminInformeRecetas"),
    path('solicitud-laboratorio/',adminSolicitudLaboratorio,name="adminSolicitudLaboratorio"),
    path('estado-laboratorio/',adminEstadoLaboratorio,name="adminEstadoLaboratorio"),

]