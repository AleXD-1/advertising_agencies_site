from django import forms

from .models import Agencies


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agencies
        exclude = ['user']
        fields = ['agency_name', 'description', 'services', 'region', 'city', 'address', 'post_index', 'work_phone',
                  'mobile_phone', 'web_site', 'user']
        widgets = {
            'agency_name': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'services': forms.Select(attrs={"class": "form-control"}),
            'region': forms.Select(attrs={"class": "form-control"}),
            'city': forms.Select(attrs={"class": "form-control"}),
            'address': forms.TextInput(attrs={"class": "form-control"}),
            'post_index': forms.TextInput(attrs={"class": "form-control"}),
            'work_phone': forms.TextInput(attrs={"class": "form-control"}),
            'mobile_phone': forms.TextInput(attrs={"class": "form-control"}),
            'web_site': forms.URLInput(attrs={"class": "form-control"}),
            'user': forms.HiddenInput()
        }
