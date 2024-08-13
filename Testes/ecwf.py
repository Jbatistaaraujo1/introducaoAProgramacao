carro = int(input("Digite sua quantidade de carros: "))
multaToltal = 0
multa = 0
while (carro != 555):
    if (carro > 2):
        multa = (carro - 2) * 10
        multaToltal = multaToltal + multa
    carro = int(input("Digite sua quantidade de carros: "))

print (f"O total da multa foi {multaToltal}.")
