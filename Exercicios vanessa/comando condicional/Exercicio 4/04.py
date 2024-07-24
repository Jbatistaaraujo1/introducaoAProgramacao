tipoParticipante = str.lower(input("Escreva o tipo de participante: "))

exAluno = 60
convi12mais = 50
convi3mais = 25
convi3menos = 0

if tipoParticipante == "ex-aluno" or "ex-aluna" or "ex aluno" or "ex aluna":
    print(f"O valor da entrada foi R$ {exAluno:.2f}")
elif tipoParticipante == "convidado":
    idade = int(input("Digite sua idade "))
    if idade >= 12:
        print(f"O valor da entrada foi de R$ {convi12mais:.2f}")
    elif idade >= 3:
        print(f"O valor da entrada foi de R$ {convi3mais:.2f}")
    else:
        print(f"O valor da entrada foi de R$ {convi3menos:.2f}")
