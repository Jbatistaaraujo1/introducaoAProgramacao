totalIdade = 0
quantPessoas = 0
quantAcima30 = 0
maiorIdade = 0
quantBom =0
for cont in range(6):
    idade = int(input("Escreva sua idade: "))
    opiniao = str.lower(input("Escreva sua opinião: "))
    if opiniao == "bom":
        totalIdade += idade
        quantBom += 1
    if (opiniao == "ruim") or (opiniao == "regular"):
        quantPessoas += 1
    if idade > 30:
        if opiniao == "excelente":
            quantAcima30 += 1
    if idade > maiorIdade:
        maiorIdade = idade
mediaBom = totalIdade // quantBom
print()
print(f"Média de idade Bom: {mediaBom}")
print(f"Quantidade respostas ruim/regular: {quantPessoas}")
print(f"Pessoas acima de 30 exelente: {quantAcima30}")
print(f"Maior idade: {maiorIdade}")