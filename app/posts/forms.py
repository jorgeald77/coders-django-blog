from django import forms
from django.forms import ModelForm
from django.db.models import Model
from django.db import models
from posts.models import BlogPost
from django.contrib.auth.models import User
from datetime import datetime


class PostForm(forms.Form):
    
    titulo = forms.CharField(max_length=25)
    contenido = forms.CharField(widget=forms.Textarea, max_length=3000)
    fecha = forms.DateField() #ver bien esto
    # autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #luego agregar lo de la imagen