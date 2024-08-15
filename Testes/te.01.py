quantRepeticoes = int(input("Quantos ingressos foram vendidos? "))
idade = int(input("Escreva a idade? "))
maior = idade
cont = 0
while (cont < quantRepeticoes):
    idade = int(input("Escreva a idade? "))
    if (idade > maior):
        maior = idade
        

    cont += 1

print(f"A maior idade foi {maior}")