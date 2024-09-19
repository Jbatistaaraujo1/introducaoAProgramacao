listaOrcamento2024 = []
quantMeses = 12
for i in range(quantMeses):
    mes = str.lower(input("Escreva o mês: "))
    receita = int(input("Escreva a receita: "))
    despesa = int(input("Escreva a despesa: "))
    listaOrcamento2024.append([mes,receita,despesa])
# O total recebido nos 5 primeiros meses
total5 = 0
for i in range(5):
    total5 += listaOrcamento2024[i][1]
print(f"o total recebido nos 5 primeiros meses foi: {total5}")
# O nome dos meses em que a despesa foi superior a R$ 2500
listaDespesaAcima = []
for i in range(quantMeses):
    if listaOrcamento2024[i][2] > 2500:
        listaDespesaAcima.append(listaOrcamento2024[i][0])
print(f"o nome dos meses em que a despesa foi superior a R$ 2500: {listaDespesaAcima}")
# A quantidade de meses em que a receita foi maior que a despesa
quantMesesReceitaMaiorDespesa = 0
for i in range(quantMeses):
    if listaOrcamento2024[i][1] > listaOrcamento2024[i][2]:
        quantMesesReceitaMaiorDespesa += 1
print(f"a quantidade de meses em que a receita foi maior que a despesa: {quantMesesReceitaMaiorDespesa}")
# O nome do mês em que houve a maior despesa
maiorDespesa = listaOrcamento2024[0][2]
for i in range(quantMesesReceitaMaiorDespesa):
    if listaOrcamento2024[i][2] > maiorDespesa:
        maiorDespesa = listaOrcamento2024[i][2]
        despesa = listaOrcamento2024[i][0]
print(f"o nome do mês em que houve a maior despesa: {despesa}")
# A receita média anual
totalReceita = 0
for i in range(quantMeses):
    totalReceita += listaOrcamento2024[i][1]
mediaReceita = totalReceita / quantMeses
print(f"a receita média anual: {mediaReceita}")