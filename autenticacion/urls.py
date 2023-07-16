from django.urls import path
from autenticacion.views import *

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_session', cerrar_session, name="cerrar_session"),
    path('logear', logear, name="logear"),

]
