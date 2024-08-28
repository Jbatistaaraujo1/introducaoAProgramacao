continuar = "sim"
quantVacinadas = 0
while continuar != "não" and continuar != "nao":
    idade = int(input("Digite a idade da criança: "))
    if (idade >= 3) and (idade <= 6):
        quantVacinadas += 1
    continuar = str.lower(input("Deseja continuar? Digite sim ou não: "))
print(f"O total de vacinas aplicadas foi de {quantVacinadas}")
