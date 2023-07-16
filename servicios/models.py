from django.db.models import *

# Create your models here.

class Servicio(Model):
    titulo = CharField(max_length=50)
    contenido = CharField(max_length=50)
    imagen = ImageField(upload_to='servicios')
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo