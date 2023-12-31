from django.shortcuts import render, redirect
from apps.contacto.forms import FormularioContacto

from django.core.mail import EmailMessage
from django.core.mail import send_mail

from techsolutions.settings import EMAIL_HOST_USER


# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            asunto = request.POST.get("asunto")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App Django",
                                 f"El usuario con el nombre {nombre} con la direccion {email} escribe lo siguiente: {asunto}\n {contenido}",
                                 "",
                                 ["isaeldiroche00@gmail.com"],
                                 reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")



    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})

# ------------------------------------------------------------------------
