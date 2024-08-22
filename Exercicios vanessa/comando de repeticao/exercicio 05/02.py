continuar = "sim"
totalArrecadado = 0
formandos = 0
totalConvidados = 0
while continuar != "não":
    quantConvi = int(input("Escreva a quantidade de convidados: "))
    if quantConvi > 15 and quantConvi < 25:
        valor = (quantConvi - 15) * 42
        totalArrecadado += valor
        totalConvidados += quantConvi
    elif quantConvi > 25:
        valor = 10 * 42
        totalArrecadado += valor
        totalConvidados += 25
    else:
        totalConvidados += quantConvi
    formandos += 1
    continuar = str.lower(input("Deseja continuar? Digite sim ou não: "))
totalConvidados += formandos
print(f"{valor:.2f}")
print(f"{totalConvidados}")