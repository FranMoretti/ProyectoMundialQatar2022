from django.shortcuts import render

# Views de Pestañas

def home(request):
    return render(request, "02-home.html")

def selecciones(request):
    return render(request, "04-selecciones.html")

def estadios(request):
    return render(request, "05-estadios.html")

def integrantes(request):
    return render(request, "08-about_us.html")
