from django.urls import path
from apps.contacto.views import *

urlpatterns = [
    path('', contacto, name="Contacto"),

]
