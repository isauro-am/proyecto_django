from django.shortcuts import render, redirect


from .models import Persona
from .forms import PersonasForm


def inicio(request):
	personas = Persona.objects.all()
	print(personas)
	contexto = {
		'personas':personas
	}
	return render(request, 'index.html',contexto)

def crearPersona(request):
	if request.method == 'GET':
		form = PersonasForm()
		contexto = {
			'form':form
		}
	else:
		form = PersonasForm(request.POST)
		
		contexto = {
			'form':form
		}
		if form.is_valid():
			form.save()
			return redirect('index')
	return render(request, 'crear_persona.html',contexto) 

# Create your views here.
def editarPersona(request,id):
	persona = Persona.objects.get(id = id)
	if request.method == 'GET':
		form = PersonasForm(instance = persona)
		contexto={
			'form':form
		}
	else:
		form = PersonasForm(request.POST, instance = persona)
		contexto = {
			'form':form
		}
		if form.is_valid():
			form.save()
			return redirect('index')
	return render(request,'crear_persona.html',contexto)

def eliminarPersona(request,id):
	persona = Persona.objects.get(id = id)
	persona.delete()
	return redirect('index')