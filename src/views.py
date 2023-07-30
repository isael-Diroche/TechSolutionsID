from django.shortcuts import render, HttpResponse
from apps.servicios.models import Servicio


# Create your views here.

def home(request):
    context = {
        'title': 'TechSolutionsID',
    }
    
    return render(request, "home/home.html", context)

# ------------------------------------------------------------------------


