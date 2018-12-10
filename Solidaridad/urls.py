"""Solidaridad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from seguridad import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.quienes_somos, name='quienes_somos'),
    url(r'^donde-estamos/$', views.donde_estamos, name='donde_estamos'),
    url(r'^donacion/$', views.donacion, name='donacion'),
    url(r'^que-hacemos/$', views.que_hacemos, name='que_hacemos'),
    url(r'^voluntario/$', views.voluntario, name='voluntario'),
    url(r'^opiniones/$', views.opiniones, name='opiniones'),
    url(r'^security/', include('seguridad.urls')),
    url(r'^application/', include('ong.urls')),
    url(r'^opiniones/$', views.opiniones, name='opiniones_cliente'),
    url(r'^opiniones_guardar/$', views.opiniones_guardar, name='opiniones_guardar'),
    url(r'^registroV_guardar/$', views.RegistroV_guardar, name='RegistroV_guardar'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
