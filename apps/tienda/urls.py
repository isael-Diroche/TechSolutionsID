from django.urls import path
from apps.tienda.views import tienda

urlpatterns = [
    path('', tienda, name="Tienda"),

]
