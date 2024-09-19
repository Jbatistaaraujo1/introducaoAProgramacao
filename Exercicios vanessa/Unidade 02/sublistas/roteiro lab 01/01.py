FuncionariosHotel = [["Guilherme Sá",26,"Segurança",852.30],
["Laura Dias",31,"Recepção",715.00],
["Sônia Lopes",44,"Lavanderia",807.90],
["Roberto Reis",22,"Garagem",475.69]]

# a)
novoSalarioLaura = float(input("Escreva o novo Salário de Laura: "))
FuncionariosHotel[1][3] = novoSalarioLaura
# b)
listanovofuncionario = []
nomenovoFuncionario = str(input("Escreva o nome do novo funcionario: "))
setornovoFuncionario = str(input("Escreva o setor do novo funcionario: "))
idadenovoFuncionario = int(input("Escreva a idade do novo funcionario: "))
salarionovoFuncionario = float(input("Escreva o salário do novo funcionario: "))
FuncionariosHotel.append([nomenovoFuncionario,idadenovoFuncionario,setornovoFuncionario,salarionovoFuncionario])
# c)
for i in range(len(FuncionariosHotel)):
    if FuncionariosHotel[i][2] == "Lavanderia":
        FuncionariosHotel[i][3] = FuncionariosHotel[i][3] + (FuncionariosHotel[i][3] * 0.1)
# d)
print(f"A idade e o salário do terceiro funcionário da lista: {FuncionariosHotel[2][1], FuncionariosHotel[2][3]}")
print()
# e)
for i in range(len(FuncionariosHotel)):
    if FuncionariosHotel[i][1] < 30 :
        print(f"Nome e setor de todos os funcionários com menos de 30 anos: {FuncionariosHotel[i][0], FuncionariosHotel[i][2]}")
        print()
# f)
for i in range(len(FuncionariosHotel)):
    if FuncionariosHotel[i][2] == "Lavanderia":
        print(f"O nome de todos os funcionários do setor de Lavanderia: {FuncionariosHotel[i][0]}")
        print()
# g)
totalIdadeGaragem = 0
totalGaragem = 0
for i in range(len(FuncionariosHotel)):
    if FuncionariosHotel[i][2] == "Garagem":
        totalGaragem +=1
        totalIdadeGaragem += FuncionariosHotel[i][1]
mediaIdadeGaragem = totalIdadeGaragem / totalGaragem
print(f"A média de idade dos funcionários do setor Garagem: {mediaIdadeGaragem}")
print()
# h)
maiorSalario = FuncionariosHotel[0][3]
for i in range(len(FuncionariosHotel)):
    if FuncionariosHotel[i][3] > maiorSalario:
        maiorSalario = FuncionariosHotel[i][3]
        nomeMaiorSalario = FuncionariosHotel[i][0]
print(f"O nome do funcionário que ganha o maior salário: {nomeMaiorSalario}")
print()
# i)
quantIdadeSalario = 0
for i in range(len(FuncionariosHotel)):
    if FuncionariosHotel[i][3] > 700:
        if FuncionariosHotel[i][1] < 40:
            quantIdadeSalario += 1
print(f"A quantidade de funcionários que ganham mais de R$ 700 e têm menos de 40 anos: {quantIdadeSalario}")
print()
# j)
maiorIdade = FuncionariosHotel[0][1]
for i in range(len(FuncionariosHotel)):
    if FuncionariosHotel[i][1] >= maiorIdade:
        maiorIdade = FuncionariosHotel[i][1]
        nomeSetorMaiorIdade = FuncionariosHotel[i][2]
print(f"Nome do setor que tem o funcionário mais velho: {nomeSetorMaiorIdade}")
print()
# k)
funcionariosAcimaMedia = []
totalSalarios = 0
for i in range(len(FuncionariosHotel)):
    totalSalarios += FuncionariosHotel[i][3]
mediaSalario = totalSalarios / len(FuncionariosHotel)
for i in range(len(FuncionariosHotel)):
    if FuncionariosHotel[i][3] > mediaSalario:
        funcionariosAcimaMedia.append(FuncionariosHotel[i][0])
print(f"Lista com o nome dos funcionários que ganham acima da média salarial da empresa: {funcionariosAcimaMedia}")
