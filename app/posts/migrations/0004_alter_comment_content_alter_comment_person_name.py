# Generated by Django 4.0.5 on 2022-06-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='person_name',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
