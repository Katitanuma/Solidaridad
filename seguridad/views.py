# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from htmlmin.decorators import minified_response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

@minified_response
def login_form(request):
	if not request.user.is_authenticated():
		form = AuthenticationForm()
		for campo in form.fields:
			form.fields[campo].widget.attrs['class'] = 'form-control'
		return render(request, 'login_form.html', {'form': form})
	else:
		return render(request, 'home.html')

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
def diseno(request, id = 0):
	if int(id) == 1:
		return HttpResponseRedirect(reverse('security:login_form'))
	else:
		if not request.user.is_authenticated():
			return HttpResponseRedirect(reverse('security:login_form'))
		else:
			return render(request, 'home.html')