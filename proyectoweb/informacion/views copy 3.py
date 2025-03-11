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
    listaJugadores=[
        {
            "Nombre":"Cristiano Ronaldo",
            "Demarcacion":"Delantero",
            "Numero": 7
        },
        {
            "Nombre": "Guti",
            "Demarcacion": "Centrocampista",
            "Numero": 14
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero":9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero":8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]

    context = {
        "jugadores": listaJugadores
    }
    return render(request, 'informacion/jugadores.html', context)

def colores(request):
    # Recuperamos la variable que nos están enviando
    # mediante GET (micolor)
    # Debemos comprobar que recibimos algo llamado "micolor"
    if ('micolor' in request.GET):
        colorRecibido = request.GET['micolor']
        # Con el colore recibido se lo devolvemos al dibujo para pintarlo
        context = {
            "colordibujo": colorRecibido
        }
        return render(request, 'informacion/colores.html', context)
    else:
        return render(request, 'informacion/colores.html')
def saludo(request):
    return render(request, 'informacion/saludo.html')