FilmesNetflix = [ ["Os Miseráveis", "Musical", 2012, 158, "Português"],
["Gravidade", "Aventura", 2013, 91, "Inglês"],
["Frozen", "Infantil", 2013, 102, "Português"],
["O Artista", "Comédia", 2011, 100, "Inglês"],
["Os Smurfs", "Infantil", 2011, 86, "Português"]]

# a)
for i in range(len(FilmesNetflix)):
    if FilmesNetflix[i][0] == "Gravidade":
        FilmesNetflix[i][3] = 95

# b)
for i in range(len(FilmesNetflix)):
    if FilmesNetflix[i][2] == 2011:
        print(f"Para cada filme de 2011, exibir título, duração e idioma: {FilmesNetflix[i][0]},{FilmesNetflix[i][3]},{FilmesNetflix[i][4]}")
print()    
# c)
menorDuracao = FilmesNetflix[1][3]
for i in range(len(FilmesNetflix)):
    if FilmesNetflix[i][4] == "Inglês":
        if FilmesNetflix[i][3] <= menorDuracao:
            menorDuracao = FilmesNetflix[i][3]
            nomeMenorDuracao = FilmesNetflix[i][0]
print(f"O nome do filme mais curto com idioma Inglês: {nomeMenorDuracao}")
print()

# d)
totalTempoInfantil = 0
for i in range(len(FilmesNetflix)):
    if FilmesNetflix[i][1] == "Infantil":
        totalTempoInfantil += FilmesNetflix[i][3]
print(f"O total em minutos que alguém levaria para assistir todos os filmes infantis: {totalTempoInfantil}")
print()

# e)
for i in range(len(FilmesNetflix)):
    if FilmesNetflix[i][4] == "Inglês":
        print(f"O título e o ano dos filmes disponíveis em inglês.: {FilmesNetflix[i][0]},{FilmesNetflix[i][2]}")
print()

# f)
quantFilmes = 0
for i in range(len(FilmesNetflix)):
    if FilmesNetflix[i][3] < 100:
        quantFilmes += 1
print(f"A quantidade de filmes com menos de 100 minutos: {quantFilmes}")
print()

# g)
for i in range(len(FilmesNetflix)):
    if FilmesNetflix[i][4] == "Português":
        if FilmesNetflix[i][2] == 2011:
            print(f"O título de todos os filmes disponíveis em português lançados em 2011: {FilmesNetflix[i][0]}")
print()

# h)
duracaoTotalInfantil = 0
totalInfantil = 0
for i in range(len(FilmesNetflix)):
    if FilmesNetflix[i][1] == "Infantil":
        duracaoTotalInfantil += FilmesNetflix[i][3]
        totalInfantil += 1
mediaDuracaoInfantil = duracaoTotalInfantil // totalInfantil
print(f"A duração média dos filmes infantis: {mediaDuracaoInfantil}")
print()

# i)
Filmes2011ate2015 = []
for i in range(len(FilmesNetflix)):
    if FilmesNetflix[i][2] >= 2012 and FilmesNetflix[i][2] <= 2015:
        Filmes2011ate2015.append(FilmesNetflix[i][1])
print(f"Uma lista com os gêneros de filmes lançados entre 2012 e 2015: {Filmes2011ate2015}")
