from django.shortcuts import render
from television.models import ServiceSeries

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def metodoSeries(request):
    servicio = ServiceSeries()
    series = servicio.getSeries()
    context = {
        "series": series
    }
    return render(request, 'pages/series.html', context)


def metodoPersonajes(request):
    servicio = ServiceSeries()
    personajes = servicio.getPersonajes()
    context = {
        "personajes": personajes
    }
    return render(request, 'pages/personajes.html', context)

def personajesSeries(request):
    # Preguntamos si hemos recibido el dato de idserie en GET
    if ('idserie' in request.GET):
        servicio = ServiceSeries()
        idserie = request.GET['idserie']
        personajes = servicio.getPersonajesSerie(idserie)
        context = {
         "personajes": personajes,
         "mensaje":"recicibdo"
        }
        return render(request, 'pages/personajesseries.html', context)
    else:
        return render(request, 'pages/personajesseries.html')
    
def modificarPersonaje(request):
    servicio = ServiceSeries()
    if ('cajaimagen' in request.POST):
        idpersonaje = request.POST['cajaidpersonaje']
        nombre = request.POST['cajanombre']
        imagen = request.POST['cajaimagen']
        idserie = request.POST['cajaserie']
        servicio.updatePersonaje(idpersonaje, nombre, imagen, idserie)
        return render(request, 'pages/modificarpersonaje.html')
    elif ('idpersonaje' in request.GET):
        idpersonaje = request.GET['idpersonaje']
        personaje = servicio.findPersonaje(idpersonaje)
        context = {
            "personaje": personaje
        }
        return render(request, 'pages/modificarpersonaje.html', context)

    else:
        return render(request, 'pages/modificarpersonaje.html')