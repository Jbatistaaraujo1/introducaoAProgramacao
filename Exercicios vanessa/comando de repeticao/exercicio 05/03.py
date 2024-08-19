entrada = str.lower(input("Crédito,débito ou sair: "))
quantCredito = 0
credito = 0
debito = 0
while (entrada != "sair"):
    quantia = float(input("Escreva a quantia: "))
    if entrada == "crédito":
        quantCredito += 1
        credito += quantia
    elif entrada == "débito":
        debito += quantia
    saldo = credito - debito
    entrada = str.lower(input("Crédito,débito ou sair: "))
print(f"A quantidade de créditos foi de : {quantCredito}")
print(f"Saldo finaceiro R$ {saldo:.2f}")
if saldo >= 0:
    print("Saldo positivo")
else:
    print("saldo negativo")
 