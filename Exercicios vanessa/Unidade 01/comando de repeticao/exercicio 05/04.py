filhos = int(input("Escreva a quantidade de filhos: "))
funcionarios = 0
quantFilhos = 0
while filhos >=0:
    quantFilhos += filhos
    funcionarios +=1
    filhos = int(input("Escreva a quantidade de filhos: "))
media = quantFilhos // funcionarios
print(f"A média de filhos : {media}")