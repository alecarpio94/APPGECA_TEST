from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseRedirect

# Create your views here.

def inicio(request):
	
	return render (request, 'pagina/inicio.html')

def contact(request):
	
	return render (request, 'pagina/contacto.html')

def frecuente(request):
	
	return render (request, 'pagina/preguntas.html')

def somos(request):
	
	return render (request, 'pagina/resena.html')

def mision(request):
	
	return render (request, 'pagina/mision.html')

def catedra1(request):
	
	return render (request, 'catedras/catedra1.html')

def catedra2(request):
	
	return render (request, 'catedras/catedra2.html')

def catedra3(request):
	
	return render (request, 'catedras/catedra3.html')

def catedra4(request):
	 
	return render(request, 'catedras/catedra4.html')
