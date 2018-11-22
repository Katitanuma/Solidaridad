# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Tipo_Voluntario(models.Model):
	tipo = models.CharField(max_length=100)

	def __str__(self):
		return self.tipo

@python_2_unicode_compatible
class Departamento(models.Model):
	depto = models.CharField(max_length=200, unique = True)

	def __str__(self):
		return self.depto

@python_2_unicode_compatible
class Sexo(models.Model):
	SEXO_CHOICES = (
		('M', 'Masculino'),
		('F', 'Femenino')
	)

	nombre = models.CharField(
		max_length=50, 
		choices=SEXO_CHOICES
	)

	def __str__(self):
		return ('Masculino' if self.nombre == 'M' else 'Femenino')

@python_2_unicode_compatible
class Voluntario(models.Model):
	identidad = models.CharField(max_length=15, blank=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	direccion = models.TextField()
	telefono = models.CharField(max_length=9)
	correo = models.EmailField(max_length=100, blank=True)
	sexo = models.ForeignKey(Sexo, on_delete = models.CASCADE)
	usuario = models.OneToOneField(User)
	depto = models.ForeignKey(Departamento)
	tipo = models.ForeignKey(Tipo_Voluntario)
	foto = models.ImageField(upload_to="fotos_voluntarios", blank=True)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return '{} {} : {}' .format(self.nombre, self.apellido, self.depto)

@python_2_unicode_compatible
class Evento(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	fecha_Hora = models.DateTimeField()
	usuario = models.ForeignKey(User)
	depto = models.ManyToManyField(Departamento)
	voluntario = models.ManyToManyField(Voluntario)

	def __str__(self):
		return '{} el dia {} en los departamentos {}' .format(self.nombre, self.fechaHora, ",".join([d.depto for d in self.depto.all()]))

class Banco_Informacion(models.Model):
	descripcion = models.CharField(max_length=100, null=True)
	archivo = models.FileField(upload_to="archivos")

	def __str__(self):
		return self.descripcion

	class Meta:
		verbose_name_plural = "Banco de información"

class Estructura_Organizativa(models.Model):
	mision = models.TextField()
	vision = models.TextField()
	politicas = models.TextField()

@python_2_unicode_compatible
class Preguntas_Frecuentes(models.Model):
	pregunta = models.TextField()
	respuesta = models.TextField()

	def __str__(self):
		return self.pregunta

@python_2_unicode_compatible
class Opiniones(models.Model):
	opinion = models.TextField()
	estado = models.BooleanField(default=False)
	fecha_hora = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.opinion

@python_2_unicode_compatible
class Auditoria(models.Model):
	usuario = models.ForeignKey(User)
	accion = models.TextField()
	fecha_hora = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' %(accion, fecha_hora)

@python_2_unicode_compatible
class Contactanos(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	telefono = models.CharField(max_length=9, blank=True)
	correo = models.EmailField(max_length=100, blank=True)
	mensaje = models.TextField()
	fecha_hora = models.DateTimeField()
	estado = models.BooleanField(default=False)

	def __str__(self):
		return '%s - %s' %(nombre, apellido)


