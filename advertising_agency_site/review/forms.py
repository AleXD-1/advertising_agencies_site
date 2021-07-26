from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude = ['agency', 'client']
        fields = ['agency', 'client', 'review_text']
        widgets = {
            'agency': forms.HiddenInput(),
            'client': forms.HiddenInput(),
            'review_text': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
