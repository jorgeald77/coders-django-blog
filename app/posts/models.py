from http import server
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=25, verbose_name='Título')
    subtitle = models.CharField(max_length=25, verbose_name='subtítulo')
    content = models.TextField(max_length=3000, verbose_name='Contenido')
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField(null=True, blank=True, verbose_name='Fecha de publicación')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    foto = models.ImageField(upload_to='posts', default='images/no-image-icon.png', null=True, verbose_name='Foto')

    def __str__(self):
        return f'User: {self.user.username} -- Titulo: {self.title} -- Contenido: {self.content[:(42-(len(self.title)-4))]} -- Fecha de publicacion: {self.published_at}'
                                                        #esa cuenta hace que no quede mal la lista cuando un titulo + el contenido
                                                        #de un posteo son muy largos, pero a la vez permite que no se le limte la
                                                        #longitud a todos.

    def get_absolute_url(self):
        return reverse('viewPosts')
    
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['created_at']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    person_name = models.CharField(max_length=255) #verbose_name='Titulo-com' (está comentado por si se necesita luego) 16
    content = models.TextField(max_length=1600) #verbose_name='Contenido-com' (está comentado por si se necesita luego)
    created_at = models.DateTimeField(auto_now_add=True) #verbose_name='Fecha de creación-com' (está comentado por si se necesita luego)

    def __str__(self):
        return f'Comentario: {self.content} -- Autor:{self.person_name}'