n1 = int(input("Escreva um número:"))
n2 = int(input("Escreva um número:"))
n3 = int(input("Escreva um número:"))

if (n1>n2) and (n1>n3):
    print(f"O maior número é o {n1}")
elif(n2>n1) and (n2>n3):
    print(f"O maior número é o {n2}")
elif(n3>n1) and (n3>n2):
    print(f"O maior número é o {n3}")