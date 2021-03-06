# Generated by Django 4.0.5 on 2022-06-17 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='profiles', verbose_name='Foto')),
                ('nombre', models.CharField(blank=True, max_length=64, null=True, verbose_name='Nombre(s)')),
                ('apellidos', models.CharField(blank=True, max_length=128, null=True, verbose_name='Apellidos')),
                ('sexo', models.CharField(choices=[('h', 'Hombre'), ('m', 'Mujer')], default=None, max_length=1, null=True, verbose_name='Sexo')),
                ('fdn', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Sitio web')),
                ('rss_facebook', models.CharField(blank=True, max_length=32, null=True, verbose_name='Facebook')),
                ('rss_twitter', models.CharField(blank=True, max_length=32, null=True, verbose_name='Twitter')),
                ('rss_instagram', models.CharField(blank=True, max_length=32, null=True, verbose_name='Instagram')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nombre', 'apellidos'],
            },
        ),
    ]
