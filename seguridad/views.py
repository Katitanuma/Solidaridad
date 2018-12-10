# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from htmlmin.decorators import minified_response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from ong.models import *
from django.template.defaultfilters import timesince, linebreaks
from .forms import *


@minified_response
def login_form(request):
	if not request.user.is_authenticated():
		form = AuthenticationForm()
		for campo in form.fields:
			form.fields[campo].widget.attrs['class'] = 'form-control'
		return render(request, 'login_form.html', {'form': form})
	else:
		return HttpResponseRedirect(reverse('app:home'))

@minified_response
def log_in(request):
	form = AuthenticationForm(data = request.POST)

	if form.is_valid():
		usuario = authenticate(username = request.POST['username'], password = request.POST['password'])

		if usuario is not None:
			if usuario.is_active:
				login(request, usuario)
				return HttpResponseRedirect(reverse('app:home'))
			else:
				for campo in form.fields:
					form.fields[campo].widget.attrs['class'] = 'form-control'
				return render(request, 'login_form.html', {'form': form, 'message': 'Usuario inactivo'})
	else:
		for campo in form.fields:
			form.fields[campo].widget.attrs['class'] = 'form-control'
		return render(request, 'login_form.html', {'form': form, 'message': 'Usuario o contraseña incorrecta'})

@minified_response
def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('security:login_form'))

@minified_response
def que_somos(request):
	return render(request, 'que_somos.html')

@minified_response
def quienes_somos(request):
	preguntas = Preguntas_Frecuentes.objects.all()
	return render(request, 'quienes_somos.html', {'preguntas': preguntas})

@minified_response
def donde_estamos(request):
	return render(request, 'donde_estamos.html')

@minified_response
def donacion(request):
	return render(request, 'donacion.html')

@minified_response
def que_hacemos(request):
	return render(request, 'que_hacemos.html')

@minified_response
def voluntario(request):
	form = RegistroForm()
	return render(request, 'voluntario.html', {'form': form})


@minified_response
def opiniones(request):
	opiniones = Opiniones.objects.order_by('-fecha_hora')
	return render(request, 'opiniones_cliente.html', {'opiniones': opiniones})
	
@minified_response
def opiniones_guardar(request):
	if request.is_ajax():
		opinion = Opiniones()
		opinion.opinion = request.GET['opinion']
		opinion.save()
		o = '''
			<div class="panel panel-default">
						  <div class="panel-body">
						  	<strong>Anónimo</strong><br>
						    {}
						    <small style="color:#9A9999">hacé {}</small>
						  </div>
			</div>
		'''.format(linebreaks(opinion.opinion), timesince(opinion.fecha_hora))
		return JsonResponse({'opinion': o})
	else:
		return HttpResponseRedirect(reverse('opiniones_cliente'))

@minified_response
def RegistroV_guardar(request):
	mensaje=''
	if request.method=='POST':
		form=RegistroForm(request.POST)

		if form.is_valid():
			form.save()
			mensaje='Datos Registrados con exito'
	else:
		mensaje='Error al registrar los datos'
	return JsonResponse({'mensaje':mensaje})
