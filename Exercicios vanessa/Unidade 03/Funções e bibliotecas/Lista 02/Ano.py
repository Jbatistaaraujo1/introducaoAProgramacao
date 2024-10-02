def defineEstacao(mes):
    inverno = ["dezembro","janeiro", "fevereiro"]
    outono = ["setembro","outubro","novembro"]
    primavera = ["março","abril","maio"]
    if mes.lower() in inverno:
        return "Inverno"
    elif mes.lower() in outono:
        return "Outono"
    elif mes.lower() in primavera:
        return "primavera"
    else:
        return "Verão"