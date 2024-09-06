lista = []
quantLetras = 5

for i in range(quantLetras):
    letras = str.lower(input("Escreva uma letra: "))
    lista.append(letras)
letraInf = str.lower(input("Digite a letra:  "))
quantInf = 0
for i in range(quantLetras):
    if lista[i] == letraInf:
        quantInf += 1
print(lista)
print()
print(f"A letra -{letraInf}- aparece na lista {quantInf} vezes")