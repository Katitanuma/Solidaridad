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
from datetime import datetime
from django.utils import timezone
from django.db.models import Sum
from django.views.generic import ListView
from django_xhtml2pdf.views import *

@minified_response
@login_required()
def home(request):
	listado1 = []
	listado2 = []
	for depto in Departamento.objects.all():
		if Voluntario.objects.filter(depto = depto).count() > 0:
			listado1.append(str(str(depto) + " ({})".format(Voluntario.objects.filter(depto = depto).count())))
			listado2.append((float(Voluntario.objects.filter(depto = depto).count()) / float(Voluntario.objects.all().count()) ) * 360 
			)

	listado3 = []
	listado4 = []
	for tipo in Tipo_Voluntario.objects.all():
		if Voluntario.objects.filter(tipo = tipo).count() > 0:
			listado3.append(str(str(tipo) + " ({})".format(Voluntario.objects.filter(tipo = tipo).count())))
			listado4.append((float(Voluntario.objects.filter(tipo = tipo).count()) / float(Voluntario.objects.all().count()) ) * 360 
			)

	listado5 = []
	listado6 = []
	listado7 = []
	for depto in Departamento.objects.all():
		if Voluntario.objects.filter(depto = depto).count() > 0:
			listado5.append(str(depto))
			listado6.append(Voluntario.objects.filter(depto = depto).count())
			listadov = []
			for v in Voluntario.objects.filter(depto = depto):
				listadov.append([str(v), Evento.objects.filter(voluntarios = v).count()])
			listado7.append(listadov)

	listado8 = []
	listado9 = [str('Enero'), str('Febrero'), str('Marzo'), str('Abril'), str('Mayo'), str('Junio'), str('Julio'), str('Agosto'), str('Septiembre'), str('Octubre'), str('Noviembre'), str('Diciembre')]
	listado10 = []
	mes = datetime.now().month
	m2 = 1

	for m in listado9:
		if m2 > mes :
			listado9.remove(m)
		m2 = m2 + 1

	for m in listado9:
		listado10.append([])

	for depto in Departamento.objects.all():
		if Evento.objects.filter(departamentos = depto).count() > 0:
			listado8.append(str(depto))
			c = 0
			for lm in listado9:
				listado10[c].append(Evento.objects.filter(departamentos = depto, fecha_Hora__month = c + 1).count())
				c = c + 1

	return render(request, 'home.html', {'deptos1': listado1, 'deptos2': listado2, 'tipo1': listado3, 'tipo2': listado4, 'd1': listado5, 'd2': listado6, 'd3': listado7, 'e1': listado8, 'e2': listado9, 'e3': listado10})

@minified_response
@login_required()
def voluntarios(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	form = VoluntarioForm()
	voluntarios = Voluntario.objects.all().order_by('nombre')
	return render(request, 'voluntarios.html', {'form': form, 'voluntarios': voluntarios})

@minified_response
@login_required()
def editarVoluntario(request, pk):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	form = VoluntarioForm(instance = Voluntario.objects.get(pk = pk))
	voluntarios = Voluntario.objects.all().order_by('nombre')
	return render(request, 'voluntarios.html', {'form': form, 'voluntarios': voluntarios, 'id': pk})

@minified_response
@login_required()
def guardarVoluntario(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
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
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	form = TipoVoluntarioForm()
	tipos = Tipo_Voluntario.objects.all().order_by('tipo')
	return render(request, 'tipos_voluntarios.html', {'form': form, 'tipos': tipos})

@minified_response
@login_required()
def editarTiposVoluntarios(request, pk):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	form = TipoVoluntarioForm(instance = Tipo_Voluntario.objects.get(pk = pk))
	tipos = Tipo_Voluntario.objects.all().order_by('tipo')
	return render(request, 'tipos_voluntarios.html', {'form': form, 'tipos': tipos, 'id': pk})

@minified_response
@login_required()
def guardarTiposVoluntarios(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
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
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	form = DepartamentoForm()
	departamentos = Departamento.objects.all().order_by('depto')
	return render(request, 'departamentos.html', {'form': form, 'departamentos': departamentos})

@minified_response
@login_required()
def editarDepartamentos(request, pk):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	form = DepartamentoForm(instance = Departamento.objects.get(pk = pk))
	departamentos = Departamento.objects.all().order_by('depto')
	return render(request, 'departamentos.html', {'form': form, 'departamentos': departamentos, 'id': pk})

@minified_response
@login_required()
def guardarDepartamentos(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
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
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	form = BancoInformacionForm(instance = Banco_Informacion.objects.get(pk = pk))
	bancos = Banco_Informacion.objects.all().order_by('descripcion')
	return render(request, 'bancos_informacion.html', {'form': form, 'bancos': bancos, 'id': pk})

@minified_response
@login_required()
def eliminarBancosInformacion(request, pk):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	banco = Banco_Informacion.objects.get(pk = pk)
	banco.delete()
	return HttpResponseRedirect(reverse('app:bancosInformacion'))

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
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
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
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
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
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	form = PreguntasFrecuentesForm()
	preguntas = Preguntas_Frecuentes.objects.all()
	return render(request, 'preguntas.html', {'form': form, 'preguntas': preguntas})

@minified_response
@login_required()
def editarPreguntas(request, pk):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	form = PreguntasFrecuentesForm(instance = Preguntas_Frecuentes.objects.get(pk = pk))
	preguntas = Preguntas_Frecuentes.objects.all()
	return render(request, 'preguntas.html', {'form': form, 'preguntas': preguntas, 'id': pk})

@minified_response
@login_required()
def guardarPreguntas(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
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

@minified_response
@login_required()
def eventos(request):
	for e in Evento.objects.filter(estado = True):
		if timezone.now() > e.fecha_Hora:
			e.estado = False
			e.save()
	form = EventoForm(initial={'usuario': request.user})
	eventos = Evento.objects.order_by('-fecha_Hora')
	return render(request, 'eventos.html', {'form': form, 'eventos': eventos})

@minified_response
@login_required()
def editarEventos(request, pk):
	for e in Evento.objects.filter(estado = True):
		if timezone.now() > e.fecha_Hora:
			e.estado = False
	form = EventoForm(instance = Evento.objects.get(pk = pk))
	eventos = Evento.objects.order_by('fecha_Hora')
	return render(request, 'eventos.html', {'form': form, 'eventos': eventos, 'id': pk})

@minified_response
@login_required()
def guardarEventos(request):
	#return HttpResponse(Departamento.objects.filter(id__in=request.POST['departamentos']))
	for e in Evento.objects.filter(estado = True):
		if timezone.now() > e.fecha_Hora:
			e.estado = False
	if request.method == 'POST':	
		form = EventoForm(data = request.POST)
		if not request.POST['id_dato'].isnumeric():
			if form.is_valid():
				form.save()
				eventos = Evento.objects.order_by('fecha_Hora')
				return render(request, 'eventos.html', {'form': EventoForm(initial={'usuario': request.user}), 'eventos': eventos, 'exito': 'Evento almacenado exitosamente!'})
			else:
				eventos = Evento.objects.order_by('fecha_Hora')
				return render(request, 'eventos.html', {'form': form, 'eventos': eventos, 'error': 'Error al almacenar el evento!'})
		else:
			form =EventoForm(data = request.POST, instance = Evento.objects.get(pk = int(request.POST['id_dato'])))
			evento = form.save(commit = False)
			evento.save()
			form.save_m2m()
			eventos = Evento.objects.order_by('fecha_Hora')
			return render(request, 'eventos.html', {'form': EventoForm(initial={'usuario': request.user}), 'eventos': eventos, 'exito': 'Evento modificado exitosamente!'})
	else:
		return render(request, '404.html')

@minified_response
@login_required()
def eliminarEventos(request, pk):
	evento = Evento.objects.get(pk = pk);
	evento.delete()
	return HttpResponseRedirect(reverse('app:eventos'))

@minified_response
@login_required()
def consultas(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	consultas = Contactanos.objects.order_by('-estado')
	return render(request, 'consultas.html', {'consultas': consultas})

@minified_response
@login_required()
def consultas_editar(request, pk):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	c = Contactanos.objects.get(pk = int(pk))
	c.estado = False
	c.save()
	return HttpResponseRedirect(reverse('app:consultas'))

@minified_response
@login_required()
def opiniones(request):
	opiniones = Opiniones.objects.order_by('-fecha_hora')
	return render(request, 'opiniones.html', {'opiniones': opiniones})

def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

@minified_response
@login_required()
def eliminarVoluntario(request, pk):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	voluntario = Voluntario.objects.get(pk = pk);
	voluntario.delete()
	return HttpResponseRedirect(reverse('app:voluntarios'))

@minified_response
@login_required()
def eliminarTipoVoluntario(request, pk):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	tipoVoluntario = Tipo_Voluntario.objects.get(pk = pk);
	tipoVoluntario.delete()
	return HttpResponseRedirect(reverse('app:tiposVoluntarios'))

@minified_response
@login_required()
def eliminarPregunta(request, pk):
	if not request.user.is_superuser:
		return HttpResponseRedirect(reverse('app:home'))
	pregunta = Preguntas_Frecuentes.objects.get(pk = pk);
	pregunta.delete()
	return HttpResponseRedirect(reverse('app:preguntas'))

class VoluntariosPdf(PdfMixin, ListView):
	model = Voluntario
	template_name = "voluntarios_pdf.html"

class EventosPdf(PdfMixin, ListView):
	model = Evento
	template_name = "eventos_pdf.html"

@minified_response
@login_required()
def usuario(request, pk):
	user = User.objects.get(pk = pk)
	return render(request, 'usuario.html', {'u': user.username, 'p': '', 'id': pk, 'is_root': user.is_superuser})

@minified_response
@login_required()
def usuarioGuardar(request):
	if request.method == 'POST':
		user = User.objects.get(pk = int(request.POST['id_dato']))
		user.username = request.POST['username']
		if str(request.POST.get('password', '')) != '' and str(request.POST.get('password2', '')) != '':
			if str(request.POST.get('password', '')) == str(request.POST.get('password2', '')) :
				user.set_password(str(request.POST.get('password', '')))
			else:
				return render(request, 'usuario.html', {'u': user.username, 'id': user.pk, 'p': '', 'is_root': user.is_superuser, 'error': 'Las Contraseñas no son iguales!'})
		if str(request.POST.get('password', '')) != '' and str(request.POST.get('password2', '')) == '':
			if str(request.POST.get('password', '')) == str(request.POST.get('password2', '')) :
				user.set_password(str(request.POST.get('password', '')))
			else:
				return render(request, 'usuario.html', {'u': user.username, 'id': user.pk, 'p': '', 'is_root': user.is_superuser, 'error': 'Las Contraseñas no son iguales!'})
		if str(request.POST.get('password', '')) == '' and str(request.POST.get('password2', '')) != '':
			if str(request.POST.get('password', '')) == str(request.POST.get('password2', '')) :
				user.set_password(str(request.POST.get('password', '')))
			else:
				return render(request, 'usuario.html', {'u': user.username, 'id': user.pk, 'p': '', 'is_root': user.is_superuser, 'error': 'Las Contraseñas no son iguales!'})
		is_root = request.POST.get('is_root', None)
		if is_root is not None:
			user.is_superuser = True
		else:
			user.is_superuser = False
		user.save()
		if not request.user.is_authenticated():
			return HttpResponseRedirect('/')
		return render(request, 'usuario.html', {'u': '', 'p': '', 'id': user.pk, 'is_root': user.is_superuser, 'exito': 'Usuario actualizado exitosamente!'})







