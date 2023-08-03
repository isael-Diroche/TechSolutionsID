from django.shortcuts import render, HttpResponse
from apps.servicios.models import Servicio
from apps.contacto.views import FormularioContacto


# Create your views here.

def home(request):
    formulario_contacto = FormularioContacto()
    context = {
        'title': 'TechSolutionsID',
        'miFormulario': formulario_contacto
    }
    
    return render(request, "home/home.html", context)

# ------------------------------------------------------------------------


