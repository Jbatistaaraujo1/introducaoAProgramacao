numero1 = input("Digite o codigo da peça1,o numero de peças e o valor unitário: ")
numero1 = numero1.split()
numero2 = input("Digite o codigo da peça1,o numero de peças e o valor unitário: ")
numero2 = numero2.split()
c1 = int(numero1[0])
n1 = int(numero1[1])
v1 = float(numero1[2])

c2 = int(numero2[0])
n2 = int(numero2[1])
v2 = float(numero2[2])

valortotal = (n1 * v1) + (n2 * v2)
print(f"VALOR A PAGAR: R$ {valortotal:.2f}")
