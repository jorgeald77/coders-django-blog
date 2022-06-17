from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    SEXO = [
        ('h', 'Hombre'),
        ('m', 'Mujer'),
    ]

    foto = models.ImageField(upload_to='profiles', null=True, blank=True, verbose_name='Foto')
    nombre = models.CharField(max_length=64, null=True, blank=True, verbose_name='Nombre(s)')
    apellidos = models.CharField(max_length=128, null=True, blank=True, verbose_name='Apellidos')
    sexo = models.CharField(max_length=1, choices=SEXO, null=True, default=None, verbose_name='Sexo')
    fdn = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')
    url = models.URLField(null=True, blank=True, verbose_name='Sitio web')
    rss_facebook = models.CharField(max_length=32, null=True, blank=True, verbose_name='Facebook')
    rss_twitter = models.CharField(max_length=32, null=True, blank=True, verbose_name='Twitter')
    rss_instagram = models.CharField(max_length=32, null=True, blank=True, verbose_name='Instagram')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Perfil de: {self.nombre} {self.apellidos}"

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['nombre', 'apellidos']
