# Inicializando uma lista vazia
numeros = []

# Solicitando ao usuário para inserir 8 números
for i in range(8):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

# Exibindo os números que são múltiplos de 3
print("Números múltiplos de 3:")
for numero in numeros:
    if numero % 3 == 0:
        print(numero)
