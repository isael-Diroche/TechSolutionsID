
def importe_total_carro(request):

    total = 0
    session = request.session
    carro = session.get("carro")
    if not carro:
        carro = session["carro"] = {}
    # else:
    carro = request.session["carro"].items()
    if request.user.is_authenticated:
        for key, value in carro:
            total = total + float(value["precio"])

    else:
        total = "Debes de iniciar seccion"

    return {"importe_total_carro": total}


