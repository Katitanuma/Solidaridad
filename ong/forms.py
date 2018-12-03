# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import *

class VoluntarioForm(ModelForm):
	class Meta:
		model = Voluntario
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super(VoluntarioForm, self).__init__(*args, **kwargs)
		for campo in self.fields:
			self.fields[campo].widget.attrs['class'] = 'form-control'
		self.fields['sexo'].choices = [('', 'Seleccione sexo')] + list(self.fields['sexo'].choices)[1:]
		self.fields['depto'].choices = [('', 'Seleccione departamento')] + list(self.fields['depto'].choices)[1:]
		self.fields['tipo'].choices = [('', 'Seleccione tipo')] + list(self.fields['tipo'].choices)[1:]
		self.fields['direccion'].widget.attrs['rows'] = '4' 
		self.fields['telefono'].label= 'Teléfono' 
		self.fields.get('usuario').widget = forms.HiddenInput()
		self.fields['depto'].label= 'Departamento' 
		self.fields['apellido'].label= 'Apellidos'
		self.fields['identidad'].widget.attrs['data-mask']='9999-9999-99999'
		self.fields['telefono'].widget.attrs['data-mask']='9999-9999'

class TipoVoluntarioForm(ModelForm):
	class Meta:
		model = Tipo_Voluntario
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super(TipoVoluntarioForm, self).__init__(*args, **kwargs)
		for campo in self.fields:
			self.fields[campo].widget.attrs['class'] = 'form-control'

class DepartamentoForm(ModelForm):
	class Meta:
		model = Departamento
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super(DepartamentoForm, self).__init__(*args, **kwargs)
		for campo in self.fields:
			self.fields[campo].widget.attrs['class'] = 'form-control'

class BancoInformacionForm(ModelForm):
	class Meta:
		model = Banco_Informacion
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super(BancoInformacionForm, self).__init__(*args, **kwargs)
		for campo in self.fields:
			self.fields[campo].widget.attrs['class'] = 'form-control'

class EstructuraOrganizativaForm(ModelForm):
	class Meta:
		model = Estructura_Organizativa
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super(EstructuraOrganizativaForm, self).__init__(*args, **kwargs)
		for campo in self.fields:
			self.fields[campo].widget.attrs['class'] = 'form-control'

class PreguntasFrecuentesForm(ModelForm):
	class Meta:
		model = Preguntas_Frecuentes
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super(PreguntasFrecuentesForm, self).__init__(*args, **kwargs)
		for campo in self.fields:
			self.fields[campo].widget.attrs['class'] = 'form-control'

class EventoForm(ModelForm):
	class Meta:
		model = Evento
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super(EventoForm, self).__init__(*args, **kwargs)
		for campo in self.fields:
			self.fields[campo].widget.attrs['class'] = 'form-control'
		self.fields['voluntarios'].widget.attrs['data-live-search'] = 'true'
		self.fields['voluntarios'].widget.attrs['class'] = 'selectpicker form-control'
		self.fields['voluntarios'].widget.attrs['title'] = u'Ningún voluntario seleccionado'
		self.fields['voluntarios'].querySet= Voluntario.objects.filter(estado = True)
		self.fields['departamentos'].widget.attrs['data-live-search'] = 'true'
		self.fields['usuario'].widget = forms.HiddenInput()
		self.fields['descripcion'].widget.attrs['rows'] = '4' 
		self.fields['fecha_Hora'].widget.attrs['size'] = '16' 
		self.fields['fecha_Hora'].widget.attrs['readonly'] = 'readonly' 
		self.fields['departamentos'].widget.attrs['class'] = 'selectpicker form-control'
		self.fields['departamentos'].widget.attrs['title'] = u'Ningún departamento seleccionado'