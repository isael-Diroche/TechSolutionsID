
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('servicios/', include('apps.servicios.urls')),

    path('blog/', include('apps.blog.urls')),

    path('contacto/', include('apps.contacto.urls')),

    path('autenticacion/', include('apps.autenticacion.urls')),

    path('tienda/', include('apps.tienda.urls')),

    path('carro/', include('carro.urls')),

    path('', include('src.urls')),

]
