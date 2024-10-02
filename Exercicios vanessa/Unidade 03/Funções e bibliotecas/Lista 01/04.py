import bibNumeros

numero = int(input("Digite um número: "))

if bibNumeros.contaDivisores(numero) == 2:
    print("Primo")
else:
    print("Não Primo")