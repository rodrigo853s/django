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
    # Debemos preguntar de forma obligatoria si hemos recibido
    # datos del formulario
    if ('cajanombre' in request.POST):
        nombreRecibido = request.POST['cajanombre']
        context = {
            "nombre": nombreRecibido
        }
        return render(request, 'informacion/saludo.html', context)
    else:
        return render(request, 'informacion/saludo.html')
    
def sumarNumeros(request):
    if ('cajanumero1' in request.POST):
        num1 = request.POST['cajanumero1']
        num2 = request.POST['cajanumero2']
        suma = int(num1) + int(num2)
        context = {
            "suma": suma
        }
        return render(request, 'informacion/sumarnumeros.html', context)
    else:
        return render(request, 'informacion/sumarnumeros.html')
    


def collatz(request):
    if ('cajanumero' in request.POST):
        dato = request.POST['cajanumero']
        numero = int(dato)
        listanumeros = []
        while (numero != 1):
            if ( numero % 2 == 0):
                numero = int(numero / 2)
            else:
                numero = int(numero * 3 + 1)
            listanumeros.append(numero)
        context = {
            "numeroscollatz": listanumeros
        }
        return render(request, 'informacion/collatz.html', context)
    else:    
        return render(request, 'informacion/collatz.html')