from django.forms import *

class FormularioContacto(Form):

    nombre = CharField(label="Nombre", required=True)

    email = EmailField(label="Email", required=True)
    
    asunto = CharField(label="Asunto", required=False)

    contenido = CharField(label="Contenido", required=True, widget=Textarea)



