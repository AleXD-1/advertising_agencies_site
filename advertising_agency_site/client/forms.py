from django import forms
from .models import Clients


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        exclude = ['user']
        fields = ['phone', 'birth_date', 'user']
        widgets = {
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'user': forms.HiddenInput()
        }
