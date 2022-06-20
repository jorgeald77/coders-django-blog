from django import forms

from blog.models import Suscriber


class FormSuscriber(forms.ModelForm):
    class Meta:
        model = Suscriber
        fields = ('nombre', 'email')
        widgets = {
            'nombre': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
        }
