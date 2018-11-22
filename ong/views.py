# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from htmlmin.decorators import minified_response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms
from .models import *
from .forms import *
import random
import string

@minified_response
@login_required()
def home(request):
	return render(request, 'home.html')

@minified_response
@login_required()
def voluntarios(request):
	form = VoluntarioForm()
	voluntarios = Voluntario.objects.all().order_by('nombre')
	return render(request, 'voluntarios.html', {'form': form, 'voluntarios': voluntarios})

@minified_response
@login_required()
def editarVoluntario(request, pk):
	form = VoluntarioForm(instance = Voluntario.objects.get(pk = pk))
	voluntarios = Voluntario.objects.all().order_by('nombre')
	return render(request, 'voluntarios.html', {'form': form, 'voluntarios': voluntarios, 'id': pk})

@minified_response
@login_required()
def guardarVoluntario(request):
	if request.method == 'POST':	
		request.POST._mutable = True
		form = VoluntarioForm(data = request.POST, files = request.FILES)
		if not request.POST['id_dato'].isnumeric():
			user = User.objects.create_user(username='User' + str(generate_key(4).lower()),
                                 email='',
                                 password='abcd123.')
			user.first_name = str(request.POST.get('nombre'))
			user.last_name = str(request.POST.get('apellido'))
			user.save()
			request.POST['usuario'] = user.id
			if form.is_valid():
				if not Voluntario.objects.filter(identidad = request.POST['identidad']).exists():
					form.save()
					voluntarios = Voluntario.objects.all().order_by('nombre')
					return render(request, 'voluntarios.html', {'form': VoluntarioForm(), 'voluntarios': voluntarios, 'exito': 'Voluntario almacenado exitosamente!'})
				else:
					user.delete()
					voluntarios = Voluntario.objects.all().order_by('nombre')
					return render(request, 'voluntarios.html', {'form': form, 'voluntarios': voluntarios, 'error': 'Ya se encuentra un voluntario registrado con esa Identidad'})
			else:
				user.delete()
				voluntarios = Voluntario.objects.all().order_by('nombre')
				return render(request, 'voluntarios.html', {'form': form, 'voluntarios': voluntarios})
		else:
			user = User.objects.get(pk = int(request.POST.get('usuario')))
			user.first_name = str(request.POST.get('nombre'))
			user.last_name = str(request.POST.get('apellido'))
			user.save()
			form = VoluntarioForm(data = request.POST, files = request.FILES, instance = Voluntario.objects.get(pk = int(request.POST['id_dato'])))
			voluntario = form.save(commit = False)
			voluntario.save()
			voluntarios = Voluntario.objects.all().order_by('nombre')
			return render(request, 'voluntarios.html', {'form': VoluntarioForm(), 'voluntarios': voluntarios, 'exito': 'Voluntario modificado exitosamente!'})
	else:
		return render(request, '404.html')

@minified_response
@login_required()
def tiposVoluntarios(request):
	form = TipoVoluntarioForm()
	tipos = Tipo_Voluntario.objects.all().order_by('tipo')
	return render(request, 'tipos_voluntarios.html', {'form': form, 'tipos': tipos})

@minified_response
@login_required()
def editarTiposVoluntarios(request, pk):
	form = TipoVoluntarioForm(instance = Tipo_Voluntario.objects.get(pk = pk))
	tipos = Tipo_Voluntario.objects.all().order_by('tipo')
	return render(request, 'tipos_voluntarios.html', {'form': form, 'tipos': tipos, 'id': pk})

@minified_response
@login_required()
def guardarTiposVoluntarios(request):
	if request.method == 'POST':	
		form = TipoVoluntarioForm(data = request.POST)
		if not request.POST['id_dato'].isnumeric():
			if form.is_valid():
				form.save()
				tipos = Tipo_Voluntario.objects.all().order_by('tipo')
				return render(request, 'tipos_voluntarios.html', {'form': TipoVoluntarioForm(), 'tipos': tipos, 'exito': 'Tipo de Voluntario almacenado exitosamente!'})
			else:
				tipos = Tipo_Voluntario.objects.all().order_by('tipo')
				return render(request, 'tipos_voluntarios.html', {'form': form, 'tipos': tipos, 'error': 'Error al almacenar el tipo de voluntario!'})
		else:
			form = TipoVoluntarioForm(data = request.POST, instance = Tipo_Voluntario.objects.get(pk = int(request.POST['id_dato'])))
			tipo_voluntario = form.save(commit = False)
			tipo_voluntario.save()
			tipos = Tipo_Voluntario.objects.all().order_by('tipo')
			return render(request, 'tipos_voluntarios.html', {'form': TipoVoluntarioForm(), 'tipos': tipos, 'exito': 'Tipo de Voluntario modificado exitosamente!'})
	else:
		return render(request, '404.html')

@minified_response
@login_required()
def departamentos(request):
	form = DepartamentoForm()
	departamentos = Departamento.objects.all().order_by('depto')
	return render(request, 'departamentos.html', {'form': form, 'departamentos': departamentos})

@minified_response
@login_required()
def editarDepartamentos(request, pk):
	form = DepartamentoForm(instance = Departamento.objects.get(pk = pk))
	departamentos = Departamento.objects.all().order_by('depto')
	return render(request, 'departamentos.html', {'form': form, 'departamentos': departamentos, 'id': pk})

@minified_response
@login_required()
def guardarDepartamentos(request):
	if request.method == 'POST':	
		form = DepartamentoForm(data = request.POST)
		if not request.POST['id_dato'].isnumeric():
			if form.is_valid():
				form.save()
				departamentos = Departamento.objects.all().order_by('depto')
				return render(request, 'departamentos.html', {'form': DepartamentoForm(), 'departamentos': departamentos, 'exito': 'Departamento almacenado exitosamente!'})
			else:
				departamentos = Departamento.objects.all().order_by('depto')
				return render(request, 'departamentos.html', {'form': form, 'departamentos': departamentos, 'error': 'Error al almacenar el departamento!'})
		else:
			form = DepartamentoForm(data = request.POST, instance = Departamento.objects.get(pk = int(request.POST['id_dato'])))
			departamento = form.save(commit = False)
			departamento.save()
			departamentos = Departamento.objects.all().order_by('depto')
			return render(request, 'departamentos.html', {'form': DepartamentoForm(), 'departamentos': departamentos, 'exito': 'Departamento modificado exitosamente!'})
	else:
		return render(request, '404.html')

@minified_response
@login_required()
def bancosInformacion(request):
	form = BancoInformacionForm()
	bancos = Banco_Informacion.objects.all().order_by('descripcion')
	return render(request, 'bancos_informacion.html', {'form': form, 'bancos': bancos})

@minified_response
@login_required()
def editarBancosInformacion(request, pk):
	form = BancoInformacionForm(instance = Banco_Informacion.objects.get(pk = pk))
	bancos = Banco_Informacion.objects.all().order_by('descripcion')
	return render(request, 'bancos_informacion.html', {'form': form, 'bancos': bancos, 'id': pk})

@minified_response
@login_required()
def descargarBancosInformacion(request, pk):
	banco = Banco_Informacion.objects.get(pk = pk)
	filename = banco.archivo.name.split('/')[-1]
	response = HttpResponse(banco.archivo, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=%s' % filename
	return response

@minified_response
@login_required()
def guardarBancoInformacion(request):
	if request.method == 'POST':	
		form = BancoInformacionForm(data = request.POST, files = request.FILES)
		if not request.POST['id_dato'].isnumeric():
			if form.is_valid():
				form.save()
				bancos = Banco_Informacion.objects.all().order_by('descripcion')
				return render(request, 'bancos_informacion.html', {'form': BancoInformacionForm(), 'bancos': bancos, 'exito': 'Banco de información almacenado exitosamente!'})
			else:
				bancos = Banco_Informacion.objects.all().order_by('descripcion')
				return render(request, 'bancos_informacion.html', {'form': form, 'bancos': bancos, 'error': 'Error al almacenar el banco de información!'})
		else:
			form = BancoInformacionForm(data = request.POST, files = request.FILES , instance = Banco_Informacion.objects.get(pk = int(request.POST['id_dato'])))
			banco = form.save(commit = False)
			banco.save()
			bancos = Banco_Informacion.objects.all().order_by('descripcion')
			return render(request, 'bancos_informacion.html', {'form': BancoInformacionForm(), 'bancos': bancos, 'exito': 'Banco de información modificado exitosamente!'})
	else:
		return render(request, '404.html')

@minified_response
@login_required()
def estructuraOrganizativa(request):
	estructura = None
	if Estructura_Organizativa.objects.all().exists():
		estructura = Estructura_Organizativa.objects.all().last()
	else:
		estructura = Estructura_Organizativa()
		estructura.mision = ""
		estructura.vision = ""
		estructura.piliticas = ""

	form = EstructuraOrganizativaForm(instance = estructura)
	return render(request, 'estructura_organizativa.html', {'form': form})

@minified_response
@login_required()
def guardarEstructuraOrganizativa(request):
	if request.method == 'POST':	
		form = EstructuraOrganizativaForm(data = request.POST)
		if form.is_valid():
			form = EstructuraOrganizativaForm(data = request.POST, instance = Estructura_Organizativa.objects.all().last())
			estructura = form.save(commit = False)
			estructura.save()
			return render(request, 'estructura_organizativa.html', {'form': form, 'exito': 'Estructura Organizativa actualizada exitosamente!'})
		else:
			return render(request, 'estructura_organizativa.html', {'form': form, 'error': 'Error al almacenar el estructura organizativa!'})
	else:
		return render(request, '404.html')

@minified_response
@login_required()
def preguntas(request):
	form = PreguntasFrecuentesForm()
	preguntas = Preguntas_Frecuentes.objects.all()
	return render(request, 'preguntas.html', {'form': form, 'preguntas': preguntas})

@minified_response
@login_required()
def editarPreguntas(request, pk):
	form = PreguntasFrecuentesForm(instance = Preguntas_Frecuentes.objects.get(pk = pk))
	preguntas = Preguntas_Frecuentes.objects.all()
	return render(request, 'preguntas.html', {'form': form, 'preguntas': preguntas, 'id': pk})

@minified_response
@login_required()
def guardarPreguntas(request):
	if request.method == 'POST':	
		form = PreguntasFrecuentesForm(data = request.POST)
		if not request.POST['id_dato'].isnumeric():
			if form.is_valid():
				form.save()
				preguntas = Preguntas_Frecuentes.objects.all()
				return render(request, 'preguntas.html', {'form': PreguntasFrecuentesForm(), 'preguntas': preguntas, 'exito': 'Pregunta almacenada exitosamente!'})
			else:
				preguntas = Preguntas_Frecuentes.objects.all()
				return render(request, 'preguntas.html', {'form': form, 'preguntas': preguntas, 'error': 'Error al almacenar la pregunta!'})
		else:
			form = PreguntasFrecuentesForm(data = request.POST, instance = Preguntas_Frecuentes.objects.get(pk = int(request.POST['id_dato'])))
			pregunta = form.save(commit = False)
			pregunta.save()
			preguntas = Preguntas_Frecuentes.objects.all()
			return render(request, 'preguntas.html', {'form': PreguntasFrecuentesForm(), 'preguntas': preguntas, 'exito': 'Pregunta modificada exitosamente!'})
	else:
		return render(request, '404.html')

def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))










