from django.forms import ModelForm
from django import forms
from .models import *

class VoluntarioForm(ModelForm):
	class Meta:
		model = Voluntario
		fields = '__all__'