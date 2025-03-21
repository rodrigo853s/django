from django.shortcuts import render
from hospitales.models import ServiceDepartamentos
from hospitales.models import ServiceHospitales

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def departamentosBBDD(request):
    servicio = ServiceDepartamentos()
    departamentos = servicio.getDepartamentos()
    context = {
        "departamentos": departamentos
    }
    return render(request, 'pages/departamentos.html', context)


def hospitalesBBDD(request):
    servicio = ServiceHospitales()
    hospitales = servicio.getHospitales()
    context = {
        "hospitales": hospitales
    }
    return render(request, 'pages/hospitales.html', context)

def insertarDepartamento(request):
    if ('cajanumero' in request.POST):
        servicio = ServiceDepartamentos()
        numero = request.POST['cajanumero']
        nombre = request.POST['cajanombre']
        localidad = request.POST['cajalocalidad']
        registros = servicio.insertDepartamento(numero, nombre, localidad)
        context = {
            "mensaje": "Registros insertados: " + str(registros) 
        }
        return render(request, 'pages/insertardepartamento.html', context)
    else:
        return render(request, 'pages/insertardepartamento.html')