total = 0
quantIdoso = 80
for cont in range(1,21,1):
    valor = float(input("Escreva a quantia doada: "))
    total += valor
total = total / quantIdoso
print(f"{total:.2f}")
