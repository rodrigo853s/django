from django.urls import path
from hospitales import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departamentos/', views.departamentosBBDD, name='departamentos'),
    path('hospitales/', views.hospitalesBBDD, name='hospitales'),
    path('insertardepartamento/', views.insertarDepartamento, name='insertardept'),
    path('deletedepartamento/', views.eliminarDepartamento, name='eliminardept'),
    path('updatedepartamento/', views.updateDepartamento, name='actualizardept'),
    path('detallesdepartamento/', views.detallesDepartamento, name='detallesdept'),
    path('empleadosdepartamento/', views.empleadosDepartamento, name='empdept')
]