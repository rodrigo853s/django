from django.urls import path
from aplicacion import views

# creamos los paths que vayamos a usar
# index es la raiz (app/)
# viernes viene debajo de app/
urlpatterns=[
    path('', views.index, name='index'),
    path('viernes/', views.metodoViernes, name='viernes'),
    path('listas/', views.metodoListas, name='listas'),
    path('pelis/', views.webPeliculas, name='pelis')
    
]

# Ahora voy al proyecto principal, webproject/urls.py