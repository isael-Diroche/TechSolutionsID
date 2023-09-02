from django.db.models import *

# Create your models here.

class CategoriaProd(Model):
    nombre = CharField(max_length=50)

    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"

    def __str__(self):
        return self.nombre

class Producto(Model):
    nombre = CharField(max_length=50)
    categorias = ForeignKey(CategoriaProd, on_delete=CASCADE)
    imagen = ImageField(upload_to="tienda", null= True, blank=True)
    descripcion = CharField(max_length=100)
    precio = FloatField()
    precio_anterior = FloatField()
    disponibilidad = BooleanField(default=True)

    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
