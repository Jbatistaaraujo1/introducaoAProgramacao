salario = int(input("Digite seu salario: "))
total = 0
for cont in range(1,13,1):
    despesas = int(input("Escreva o valor das despesas: "))
    Economizado = salario - despesas
    total += Economizado
    totalEconomizado = total / cont
print(f"{totalEconomizado:.2f}")
