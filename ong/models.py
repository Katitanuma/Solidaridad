# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class TipoVoluntario(models.Model):
	tipo = models.CharField(max_length=100)

	def __str__(self):
		return self.tipo

@python_2_unicode_compatible
class Departamento(models.Model):
	depto = models.CharField(max_length=200)

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
		return self.nombre

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
	tipo = models.ForeignKey(TipoVoluntario)

	def __str__(self):
		return '{} {} : {}' .format(self.nombre, self.apellido, self.depto)

@python_2_unicode_compatible
class Evento(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField()
	fechaHora = models.DateTimeField()
	usuario = models.ForeignKey(User)
	depto = models.ManyToManyField(Departamento)
	voluntario = models.ManyToManyField(Voluntario)

	def __str__(self):
		return '{} el dia {}' .format(self.nombre, self.fechaHora, ",".join([d.depto for d in self.depto.all()]))

class BancoInformacion(models.Model):
	archivo = models.FileField(upload_to="archivos")

	class Meta:
		verbose_name_plural = "Banco de información"
