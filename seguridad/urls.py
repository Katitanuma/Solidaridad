from django.conf.urls import url
from . import views

app_name = "security"

urlpatterns = [
	url(r'^$', views.login_form, name = 'login_form'),
	url(r'^log_in/$', views.log_in, name = 'log_in'),
	url(r'^log_out/$', views.log_out, name = 'log_out'),
]