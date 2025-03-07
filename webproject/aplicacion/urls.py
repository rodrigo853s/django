from django.urls import path
from aplicacion import views

# creamos los paths que vayamos a usar
# index es la raiz (app/)
# viernes viene debajo de app/
urlpatterns=[
    path('', views.index, name='index'),
    path('viernes/', views.metodoViernes, name='viernes')
    
]

# Ahora voy al proyecto principal, webproject/urls.py