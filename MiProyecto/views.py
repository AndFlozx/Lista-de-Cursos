from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

cursos = [
    [ "Desarrollo Web" , "4" , "Presencial", "Teorico-Practico", "Doc. Identificacion, Bachiller, Pruebas de Seleccion, Nivel de Educacion" ],
    [ "Idiomas" , "2" , "Virtual", "Teorico", "Doc. Identificacion, Bachiller, Pruebas de Seleccion, Nivel de Educacion " ],
]
#Request:Peticion
#HttpResponse: Respuesta en HTTP

# Primera vista #Toda funcion que 
def bienvenida(request): #Objeto de tipo request como primer argumento
    return HttpResponse("Bienvenido a su proyecto Django")

def sumaNumeros(request):
    numero_uno = 2
    numeros_dos = 3
    suma = numero_uno + numeros_dos
    resultado = "<h1> La suma de los dos numeros es: %s </h1>" %suma
    return HttpResponse(resultado)

def primeraPlantilla(request):
    return render(request, 'primeraPlantilla.html', {"cursos":cursos})

#Metodo par retornar el template
def plantillaAgregarElemento(request):
    return render(request, 'agregarElemento.html')

#Metodo para agregar a la lista
def agregarElemento(request):
    nombre = request.POST.get('nombre')
    creditos = request.POST.get('no. de creditos')
    modalidad = request.POST.get('modalidad')
    tipo_curso = request.POST.get('tipo de curso')
    requerimientos = request.POST.get('requerimientosp')
    nuevo_registro = [nombre, creditos, modalidad, tipo_curso, requerimientos]
    cursos.append(nuevo_registro)
    nuevo_elemento = request.POST.get('nuevo_elemento')
    cursos.append(nuevo_elemento)
    return redirect('primera_plantilla') # Redireccion a la pagina principal

#Metodo para eliminar el ultimo elemento de la lista
def eliminarElemento(request):
    cursos.pop()
    #lenguajes = lenguajes[:-1]
    return redirect('primera_plantilla')#Redirecciona a la pagina principal
    
