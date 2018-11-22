from django.conf.urls import url
from . import views

app_name = "app"

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^voluntarios/$', views.voluntarios, name = 'voluntarios'),
	url(r'^voluntarios/guardar/$', views.guardarVoluntario, name = 'guardarVoluntario'),
	url(r'^voluntarios/editar/(?P<pk>\d+)/$', views.editarVoluntario, name = 'editarVoluntario'),
	url(r'^tipos-voluntarios/$', views.tiposVoluntarios, name = 'tiposVoluntarios'),
	url(r'^tipos-voluntarios/guardar/$', views.guardarTiposVoluntarios, name = 'guardarTiposVoluntarios'),
	url(r'^tipos-voluntarios/editar/(?P<pk>\d+)/$', views.editarTiposVoluntarios, name = 'editarTiposVoluntarios'),
	url(r'^departamentos/$', views.departamentos, name = 'departamentos'),
	url(r'^departamentos/guardar/$', views.guardarDepartamentos, name = 'guardarDepartamentos'),
	url(r'^departamentos/editar/(?P<pk>\d+)/$', views.editarDepartamentos, name = 'editarDepartamentos'),
	url(r'^bancos-informacion/$', views.bancosInformacion, name = 'bancosInformacion'),
	url(r'^bancos-informacion/guardar/$', views.guardarBancoInformacion, name = 'guardarBancoInformacion'),
	url(r'^bancos-informacion/editar/(?P<pk>\d+)/$', views.editarBancosInformacion, name = 'editarBancosInformacion'),
	url(r'^bancos-informacion/descargar/(?P<pk>\d+)/$', views.descargarBancosInformacion, name = 'descargarBancosInformacion'),
	url(r'^estructura-organizativa/guardar/$', views.guardarEstructuraOrganizativa, name = 'guardarEstructuraOrganizativa'),
	url(r'^estructura-organizativa/$', views.estructuraOrganizativa, name = 'estructuraOrganizativa'),
	url(r'^preguntas-frecuentes/$', views.preguntas, name = 'preguntas'),
	url(r'^preguntas-frecuentes/guardar/$', views.guardarPreguntas, name = 'guardarPreguntas'),
	url(r'^preguntas-frecuentes/editar/(?P<pk>\d+)/$', views.editarPreguntas, name = 'editarPreguntas'),
]