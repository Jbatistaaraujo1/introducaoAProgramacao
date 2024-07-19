pesototal = int(input("Peso total do prato: "))

pesoprato = 230
pesoQuilo = 40
pesoGrama = pesoQuilo / 1000
pesocomida = pesototal - pesoprato
valor = pesocomida*pesoGrama

print(f"PESO TOTAL: {valor:.2f}")
