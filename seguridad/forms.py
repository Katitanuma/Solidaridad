from django.forms import ModelForm
from django import forms
from ong.models import *

class RegistroForm(ModelForm):
	class Meta:
		model = Contactanos
		fields = '__all__'
	def __init__(self, *args, **kwargs):
		super(RegistroForm, self).__init__(*args, **kwargs)
		for campo in self.fields:
			self.fields[campo].widget.attrs['class'] = 'form-control'
			self.fields['estado'].widget = forms.HiddenInput()
			self.fields['estado'].label = ""
			self.fields['mensaje'].widget.attrs['rows'] = '4' 