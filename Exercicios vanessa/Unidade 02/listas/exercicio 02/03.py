quantFuncionarios = 3
listaSetores = []
listaSalarios = []

for cont in range(quantFuncionarios):
    setor = str.lower(input("Escreva o setor: "))
    salario = int(input("Escreva o salario: "))
    listaSetores.append(setor)
    listaSalarios.append(salario)
aumentototal = 0
for i in range(quantFuncionarios):
    if listaSetores[i] == "recursos humanos" or listaSetores[i] == "almoxarifado":
        aumento = (listaSalarios[i] * 0.2)
        novoSalario = aumento + listaSalarios[i]
        aumentototal += aumento
        print(f"R$ {novoSalario:.0f}")
print(f"R$ {aumentototal:.0f}")