from django import forms
from .models import Driver,Bus
from django.forms import ModelForm


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'