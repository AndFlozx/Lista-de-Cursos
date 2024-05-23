"""
URL configuration for MiProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MiProyecto.views import bienvenida
from MiProyecto.views import sumaNumeros
from MiProyecto.views import primeraPlantilla
from MiProyecto.views import plantillaAgregarElemento
from MiProyecto.views import agregarElemento
from MiProyecto.views import eliminarElemento


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('suma/',sumaNumeros),
    path('primera_plantilla/', primeraPlantilla,name='primera_plantilla'),
    # Ruta para visualizar el formulario
    path('plantilla_agregar/', plantillaAgregarElemento,name='plantilla_agregar'),
    # Ruta para almacenar el elemento de la lista
    path('agregar_elemento/', agregarElemento,name='agregar_elemento'),   
    #Eliminar el ultimo elemento de la lista
    path('eliminar_elemento/', eliminarElemento,name='eliminar_elemento'), 
]
