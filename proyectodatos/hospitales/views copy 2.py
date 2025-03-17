from django.shortcuts import render
from hospitales.models import ServiceDepartamentos, ServiceHospitales, ServiceEmpleados



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
        departamentos = servicio.getDepartamentos
        context = {
        # "mensaje": "Registros insertados: " + str(registros)
        "departamentos": departamentos
        }
        return render(request, 'pages/departamentos.html', context)
    else:
        return render(request, 'pages/insertardepartamento.html')
    
def eliminarDepartamento(request):
    if ('cajanumero' in request.POST):
        servicio = ServiceDepartamentos()
        numero = request.POST['cajanumero']
        registros = servicio.eliminarDepartamento(numero);
        context = {
            "mensaje": "Registros eliminados: " + str(registros)
        }
        return render(request, 'pages/deletedepartamento.html', context)
    elif ('id' in request.GET):
        numero = request.GET['id']
        context = {
            "numero": numero
        }
        return render(request, 'pages/deletedepartamento.html', context)
    else:
        return render(request, 'pages/deletedepartamento.html')

def updateDepartamento(request):
    servicio = ServiceDepartamentos()
    if ('cajanumero' in request.POST):        
        numero = request.POST['cajanumero']
        nombre = request.POST['cajanombre']
        localidad = request.POST['cajalocalidad']
        registros = servicio.actualizarDepartamento(numero, nombre, localidad)
        departamentos = servicio.getDepartamentos
        context = {
        #"departamentos": departamentos
        "mensaje": "Registros insertados: " + str(registros)
        }
    elif ('id' in request.GET):
        numero = request.GET['id']
        departamento = servicio.detallesDepartamento(numero)
        context = {
            "departamento": departamento
        }
        #return render(request, 'pages/departamentos.html', context)
        return render(request, 'pages/updatedepartamento.html', context)
    else:
        return render(request, 'pages/updatedepartamento.html')
    

def detallesDepartamento(request):
    if ('id' in request.GET):
        servicio = ServiceDepartamentos()
        numero = request.GET['id']
        departamento = servicio.detallesDepartamento(numero)
        context = {
            "departamento": departamento
        }
        return render(request, 'pages/detallesdepartamento.html', context)
    else:
        return render(request, 'pages/detallesdepartamento.html')
    
def empleadosDepartamento(request):
    servicio = ServiceEmpleados()
    if ('iddepartamento' in request.POST):
        numero = request.POST['iddepartamento']
        empleados = servicio.getEmpleadosDepartamento(numero)
        context = {
            "empleados": empleados
        }
    else:
        empleados = servicio.getEmpleados()
        context = {
            "empleados": empleados
        }
    return render(request, 'pages/empleadosdepartamento.html', context)
