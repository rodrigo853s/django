from django.shortcuts import render
# Incluimos este import
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("¡¡¡ Mi primera página Django !!!")

def metodoViernes(request):
    return HttpResponse("Thanks God it's Friday !!!")

# y nos vamos a aplicacion/urls.py y lo rellenamos, que está vacío


