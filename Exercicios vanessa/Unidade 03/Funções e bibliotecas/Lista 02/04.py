import Ano
visitantesPrimavera = 0
visitantesInverno = 0
visitantesVerao = 0
visitantesOutono = 0
for i in range(6):
    mes = str.lower(input("Digite o mês: "))
    visitantes = int(input("Digite a quantidade de visitantes: "))
    if Ano.defineEstacao(mes) == "Inverno":
        visitantesInverno += visitantes
    elif Ano.defineEstacao(mes) == "Verão":
        visitantesVerao += visitantes
    elif Ano.defineEstacao(mes) == "Outono":
        visitantesOutono += visitantes
    else:
        visitantesPrimavera += visitantes
if visitantesInverno > visitantesOutono and visitantesInverno > visitantesPrimavera and visitantesInverno > visitantesVerao:
    print("Inverno")
elif visitantesVerao > visitantesOutono and visitantesVerao > visitantesPrimavera and visitantesVerao > visitantesInverno:
    print("Verão")
elif visitantesOutono > visitantesInverno and visitantesOutono > visitantesPrimavera and visitantesOutono > visitantesVerao:
    print("Outono")
else:
    print("Primavera") 