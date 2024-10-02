import Ano
totalVisitantesPrimavera = 0
for i in range(6):
    mes = str.lower(input("Digite o mês: "))
    visitantes = int(input("Digite a quantidade de visitantes: "))
    if Ano.defineEstacao(mes) == "primavera":
        totalVisitantesPrimavera += visitantes
print(totalVisitantesPrimavera)