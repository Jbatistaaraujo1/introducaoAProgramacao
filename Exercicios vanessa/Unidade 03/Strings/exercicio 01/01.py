Pessoa = [["Dilane", 30, ["João", "Denise"]],["Tibério", 28, ["Fábio", "Lúcia"]],["Gorete", 29,
["Ricardo", "Bárbara"]]]
#a)ci
print(Pessoa[1][2][1][2:4]) 
#b)3
print(Pessoa[2][0].find("e"))
#c)ooo
print(Pessoa[0][2][0][1]*3)
#d)28
print(Pessoa[2][1] - Pessoa[1][2][0].count("b"))