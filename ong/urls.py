from django.conf.urls import url
from . import views

app_name = "app"

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^voluntarios/$', views.voluntarios, name = 'voluntarios'),
	url(r'^voluntarios/guardar/$', views.guardarVoluntario, name = 'guardarVoluntario'),
	url(r'^voluntarios/editar/(?P<pk>\d+)/$', views.editarVoluntario, name = 'editarVoluntario'),
]