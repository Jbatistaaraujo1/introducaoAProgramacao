import EditoraRevistas

revistas = [["Tech Today", "Tecnologia", 5000, 29.90], ["Nature News", "Ciência", 3000,
35.00], ["Health & Life", "Saúde", 4000, 25.50], ["Fashion Forward", "Moda", 6000,
40.00], ["Sports Weekly", "Esportes", 7000, 22.00], ["Business Insight", "Negócios",
5500, 32.50]]

print(EditoraRevistas.PesquisaRevista(revistas,"Tech Today"))
print()
print(EditoraRevistas.PesquisaRevistasTema(revistas,"Saúde"))
print()
print(EditoraRevistas.PesquisaRevistasTitulo(revistas, "N"))
print()
print(EditoraRevistas.PesquisaRevistasPreco(revistas, 26))
print()
print(EditoraRevistas.CalculaTotalExemplares(revistas,"Business Insight"))
print()
print(EditoraRevistas.CalculaPrecoMedio(revistas, "Business Insight"))