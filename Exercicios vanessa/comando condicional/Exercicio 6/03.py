quantLivros = int(input("Escreva a quantidade de livros: "))
quantAlunos = int(input("Escreva a quantidade de alunos: "))

valor = quantLivros // quantAlunos

if valor <= 8:
    print("A")
elif valor <=12 :
    print("B")    
elif valor <=18:
    print("C")
elif valor > 18:
    print("D")
    