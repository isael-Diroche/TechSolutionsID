# Generated by Django 4.0.4 on 2023-09-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_created_producto_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='descripcion', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_anterior',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
