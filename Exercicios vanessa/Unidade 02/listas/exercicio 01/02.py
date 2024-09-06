lista = []

for i in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)
menorNumero = lista[0]
for i in range(len(lista)):
    if menorNumero > lista[i]:
        menorNumero = lista[i]

print(f"O menor número é {menorNumero}")
