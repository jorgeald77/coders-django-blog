from django import forms

from profiles.models import Profile


class FormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('foto', 'nombre', 'apellidos', 'sexo', 'fdn', 'descripcion', 'url', 'rss_facebook', 'rss_twitter',
                  'rss_instagram')
        widgets = {
            'foto': forms.FileInput(),
            'fdn': forms.DateInput(attrs={'type': 'date'}),
            'url': forms.URLInput(attrs={'type': 'url'})
        }
