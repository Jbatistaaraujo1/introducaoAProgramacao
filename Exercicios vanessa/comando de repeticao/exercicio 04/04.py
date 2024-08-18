cont = 0
aprovados = 0
mediaGeral = 0
maiorMedia = 0
while (cont < 50):
    nota1 = float(input("Nota 01: "))
    nota2 = float(input("Nota 02: "))
    nota3 = float(input("Nota 03: "))
    nota4 = float(input("Nota 04: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 8.00:
        print(f"O aluno teve média {media:.2f} e foi aprovado" )
        aprovados += 1
    else:
        print(f"O aluno teve média {media:.2f} e foi reprovado" )
    if media > maiorMedia:
        maiorMedia = media
    mediaGeral += media
    cont +=1
mediaTurma = mediaGeral / cont
print(f"Alunos aprovados: {aprovados}")
print(f"Média da turma: {mediaTurma:.2f}")
print(f"A maior média obtida: {maiorMedia}")
