from django.db import models


class Suscriber(models.Model):
    nombre = models.CharField(max_length=64, verbose_name='Nombre')
    email = models.EmailField(max_length=64, unique=True, verbose_name='Correo electrónico')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Suscriptor: {self.nombre}"

    class Meta:
        db_table = 'suscribers'
        verbose_name = 'Suscriber',
        verbose_name_plural = 'Suscribers'
        ordering = ['nombre']
