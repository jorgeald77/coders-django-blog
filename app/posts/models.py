<<<<<<< HEAD
from http import server
=======
from ckeditor.fields import RichTextField
>>>>>>> 398b73e812eadb45c4e525cec062eb11a9109357
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
<<<<<<< HEAD

    title = models.CharField(max_length=25, verbose_name='Título')
    content = models.TextField(max_length=3000, verbose_name='Contenido')
=======
    title = models.CharField(max_length=25, verbose_name='Título')
    content = RichTextField(max_length=3000, verbose_name='Contenido')
>>>>>>> 398b73e812eadb45c4e525cec062eb11a9109357
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField(null=True, blank=True, verbose_name='Fecha de publicación')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    foto = models.ImageField(upload_to='posts', default='images/no-image-icon.png', null=True, verbose_name='Foto')

    def __str__(self):
<<<<<<< HEAD
        return f'User: {self.user.username} -- Titulo: {self.title} -- Contenido: {self.content[:(42-(len(self.title)-4))]} -- Fecha de publicacion: {self.published_at}'
                                                        #esa cuenta hace que no quede mal la lista cuando un titulo + el contenido
                                                        #de un posteo son muy largos, pero a la vez permite que no se le limte la
                                                        #longitud a todos.

    def get_absolute_url(self):
        return reverse('viewPosts')
    
=======
        return f'User: {self.user.username} -- Titulo: {self.title} -- Contenido: {self.content[:(42 - (len(self.title) - 4))]} -- Fecha de publicacion: {self.published_at}'

    def get_absolute_url(self):
        return reverse('viewPosts')

>>>>>>> 398b73e812eadb45c4e525cec062eb11a9109357
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
<<<<<<< HEAD
        ordering = ['created_at']
=======
        ordering = ['-published_at']
>>>>>>> 398b73e812eadb45c4e525cec062eb11a9109357
