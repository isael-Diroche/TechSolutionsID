from django.forms import *

class FormularioContacto(Form):

    nombre = CharField(label="Nombre", required=True)

    email = EmailField(label="Email", required=True)

    contenido = CharField(label="Contenido", widget=Textarea)



