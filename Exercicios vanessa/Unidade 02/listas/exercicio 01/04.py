lista = []
quantNotas = 5
notasAcima = 0
for cont in range(quantNotas):
    nota = float(input(f"Escreva a nota: "))
    lista.append(nota)

for i in range(quantNotas):
    if lista[i] > 8.0:
        notasAcima += 1
print(f"A quantidade de notas acima de 8 foi: {notasAcima} ")