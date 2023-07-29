from django.shortcuts import render
from apps.servicios.models import Servicio
# Create your views here.

def servicios(request):
    servicios = Servicio.objects.all()

    return render(request, "servicios/servicios.html", {'servicios': servicios})


# ------------------------------------------------------------------------