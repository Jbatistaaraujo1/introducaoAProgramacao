Valor = 3.75
vagas = 42
quantVei = int(input("Quantidade de carros estacionados: "))

valorMomento = Valor * quantVei
vagaslivres = vagas - quantVei
totalAserganho = vagaslivres * Valor

print(f"Total até o momento: R$ {valorMomento:.2f}")
print(f"Quantidade de vagas livres: {vagaslivres}")
print(f"Total a ser ganho: R$ {totalAserganho:.2f}")