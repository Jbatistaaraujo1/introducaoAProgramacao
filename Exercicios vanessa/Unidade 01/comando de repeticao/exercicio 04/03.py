cont = 0
pontosM = 0
while (cont < 120):
    nome = str(input("Escreva o nome do competidor: "))
    pontuacao = int(input("Escreva a pontuação do competidor: "))
    if pontosM < pontuacao:
        pontosM = pontuacao
        vencedor = nome
    cont += 1
print(f"{vencedor} venceu a competição com {pontosM} pontos")
