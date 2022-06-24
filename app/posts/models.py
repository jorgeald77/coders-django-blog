from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class BlogPost(models.Model): #posteo, no formulario, eso esta en forms.py

    titulo = models.CharField(max_length=25)
    contenido = models.TextField(max_length=3000)
    fecha = models.DateField() #ver bien esto

    def __str__(self):
        return f'Titulo: {self.titulo} -- Contenido: {self.contenido[:42]} -- Fecha de publicacion: {self.fecha}'
    # autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #agregar imagefield models.ImageField(upload_to='posts')
    #mas info de imagefield en documentacion de django