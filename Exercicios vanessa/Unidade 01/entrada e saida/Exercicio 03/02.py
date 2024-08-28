quantRev = int(input("Total de revistas: "))
quantAmig = int(input("Quantidade de amigos: "))

revistasDoadas = quantRev // quantAmig
resto = quantRev % quantAmig

print(f"Revistas doadas a cada amigo: {revistasDoadas}")
print(f"Revistas Restantes: {resto}")
