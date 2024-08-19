continuar = "sim"
total = 0
formandos = 0
pessoas = 0
while continuar != "não":
    quantConvi = int(input("Escreva a quantidade de convidados: "))
    if quantConvi > 15 and quantConvi < 25:
        valor = (quantConvi - 15) * 42
        total += valor
        pessoas += quantConvi
    elif quantConvi > 25:
        valor = 10 * 42
        total += valor
        pessoas += 25
    else:
        pessoas += quantConvi
    formandos += 1
    continuar = str.lower(input("Deseja continuar? Digite sim ou não: "))
pessoas += formandos
print(f"{valor:.2f}")
print(f"{pessoas}")