lista = []
quantTurmas = 4

for cont in range(quantTurmas):
    alunos = int(input("Escreva o total de alunos de uma turma: "))
    lista.append(alunos)
totalalunos = lista[0] + lista[1] + lista[2] + lista[3]
print(f"O total de alunos das {quantTurmas} turmas foi: {totalalunos}")