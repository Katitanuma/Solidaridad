# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import *
from .forms import *

@login_required()
def home(request):
	return render(request, 'home.html')

@login_required()
def voluntarios(request):
	form = VoluntarioForm()
	voluntarios = Voluntario.objects.all().order_by('nombre')
	for campo in form.fields:
		form.fields[campo].widget.attrs['class'] = 'form-control'
	form.fields['sexo'].choices = [('', 'Seleccione sexo')] + list(form.fields['sexo'].choices)[1:]
	form.fields['depto'].choices = [('', 'Seleccione departamento')] + list(form.fields['depto'].choices)[1:]
	form.fields['tipo'].choices = [('', 'Seleccione tipo')] + list(form.fields['tipo'].choices)[1:]
	form.fields['direccion'].widget.attrs['rows'] = '4' 
	form.fields['telefono'].label= 'Teléfono' 
	form.fields['depto'].label= 'Departamento' 
	form.fields['identidad'].widget.attrs['data-mask']='9999-9999-99999'
	return render(request, 'voluntarios.html', {'form': form, 'voluntarios': voluntarios})

@login_required()
def editarVoluntario(request, pk):
	form = VoluntarioForm(instance = Voluntario.objects.get(pk = pk))
	voluntarios = Voluntario.objects.all().order_by('nombre')
	for campo in form.fields:
		form.fields[campo].widget.attrs['class'] = 'form-control'
	form.fields['sexo'].choices = [('', 'Seleccione sexo')] + list(form.fields['sexo'].choices)[1:]
	form.fields['depto'].choices = [('', 'Seleccione departamento')] + list(form.fields['depto'].choices)[1:]
	form.fields['tipo'].choices = [('', 'Seleccione tipo')] + list(form.fields['tipo'].choices)[1:]
	form.fields['direccion'].widget.attrs['rows'] = '4' 
	form.fields['telefono'].label= 'Teléfono' 
	form.fields['depto'].label= 'Departamento' 
	return render(request, 'voluntarios.html', {'form': form, 'voluntarios': voluntarios, 'id': pk})

@login_required()
def guardarVoluntario(request):
	if request.method == 'POST':	
		form = VoluntarioForm(data = request.POST, files = request.FILES)

		if form.is_valid():
			if not request.POST['id_dato'].isnumeric():
				if not Voluntario.objects.filter(identidad = request.POST['identidad']).exists():
					form.save()
				else:
					return HttpResponseRedirect(reverse('app:voluntarios'))
			else:
				form = VoluntarioForm(data = request.POST, files = request.FILES, instance = Voluntario.objects.get(pk = int(request.POST['id_dato'])))
				voluntario = form.save(commit = False)
				voluntario.save()
			return HttpResponseRedirect(reverse('app:voluntarios'))
		else:
			return HttpResponseRedirect(reverse('app:voluntarios'))
	else:
		return render(request, '404.html')










