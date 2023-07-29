from django.contrib.admin import *
from apps.tienda.models import *

# Register your models here.

class CategoriaAdmin(ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProductoAdmin(ModelAdmin):
    readonly_fields = ('created', 'updated')


site.register(CategoriaProd, CategoriaAdmin)
site.register(Producto, ProductoAdmin)
