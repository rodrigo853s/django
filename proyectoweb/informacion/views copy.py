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
    context = {
        "numeros": [ 4,6,12,98,123 ]
    }
    return render(request, 'informacion/jugadores.html', context)
