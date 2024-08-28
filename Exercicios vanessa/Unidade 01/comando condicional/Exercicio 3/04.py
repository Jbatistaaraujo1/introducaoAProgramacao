valorDiaria = int(input("Valor da diária: "))
quantDias = int(input("Quantidade de dias: "))
tempo = int(input("Tempo de atraso: "))
horas2 = 30
horas3 = 80
horas3_ = 40 #por hora
if (tempo < 2):
    valor = (valorDiaria * quantDias) + horas2
    print(f"Valor: R$ {valor:.2f}")
elif(tempo >= 2) and (tempo <= 3):
    valor = (valorDiaria * quantDias) + horas3
    print(f"Valor: R$ {valor:.2f}")
else:
    valor = (valorDiaria * quantDias) + (horas3_*tempo)
    print(f"Valor: R$ {valor:.2f}")
