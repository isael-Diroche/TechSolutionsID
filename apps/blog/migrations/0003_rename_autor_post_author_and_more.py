# Generated by Django 4.0.4 on 2023-08-09 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_categoria_contenido_remove_categoria_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='badge',
            new_name='categorias',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='contenido',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
    ]
