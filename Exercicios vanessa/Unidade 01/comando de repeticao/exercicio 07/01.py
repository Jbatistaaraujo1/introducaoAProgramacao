CRA = float (input ("Seu CRA: "))
quantNaoConcorre = 0
quantConcorre = 0
somaCraConcorre = 0
somaCraNaoConcorre = 0
while CRA >= 0:
    if (CRA >= 7.0):
        print ("Pode concorrer")
        quantConcorre += 1
        somaCraConcorre += CRA
    else:
        print ("Não pode concorrer")
        quantNaoConcorre += 1
    CRA = float (input ("Seu CRA: "))
    media = somaCraConcorre / quantConcorre
print(f"Quantidade de pessoas que não concorre a bolsa: {quantNaoConcorre}")
print(f"Média do CRA dos concorrentes: {media}")
