from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'informacion/index.html')

def pelis(request):
    return render(request, 'informacion/pelis.html')

def futbol(request):
    nombre = "Club Atlético Independiente"
    data = {
        "equipo": nombre
    }
    return render(request, 'informacion/futbol.html', data)

def jugadores(request):
    personas = [
        { "nombre": "Lucia", "edad": 22},
        { "nombre": "Temistocles", "edad": 120},
        { "nombre": "Elvira", "edad": 34}
    ]
    context = {
        "personas": personas
    }
    return render(request, 'informacion/jugadores.html', context)
