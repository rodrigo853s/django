from django.shortcuts import render
# Incluimos este import
from django.http import HttpResponse

# Create your views here.
#def index(request):
#   return HttpResponse("¡¡¡ Mi primera página Django !!!")

def index(request):
   return render(request, 'myapp/indice.html')

#def metodoViernes(request):
 #   return HttpResponse("Thanks God it's Friday !!!")

def metodoViernes(request):
    return render(request, 'myapp/viernes.html')

# y nos vamos a aplicacion/urls.py y lo rellenamos, que está vacío

def metodoListas(request):
    return render(request, 'myapp/listas.html')
    




