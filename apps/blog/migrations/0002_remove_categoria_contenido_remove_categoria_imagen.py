# Generated by Django 4.0.4 on 2022-04-22 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='imagen',
        ),
    ]