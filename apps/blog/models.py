from django.db.models import *
from django.contrib.auth.models import User

# Create your models here.

class Categoria(Model):
    nombre = CharField(max_length=50)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Post(Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    imagen = ImageField(upload_to='blog', null=True, blank=True)
    author = ForeignKey(User, on_delete=CASCADE)
    badge = ManyToManyField(Categoria)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title