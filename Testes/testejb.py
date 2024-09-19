FuncionariosHotel = [ [ "Guilherme Sá", 26, "Segurança", 852.30 ],
[ "Laura Dias", 31, "Recepção", 715.00 ],
[ "Sônia Lopes", 44, "Lavanderia", 807.90 ],
[ "Roberto Reis", 22, "Garagem", 475.69 ] ]


funcionariosAcimaMedia = []
totalSalarios = 0
for i in range(len(FuncionariosHotel)):
    totalSalarios += FuncionariosHotel[i][3]
mediaSalario = totalSalarios / len(FuncionariosHotel)
for i in range(len(FuncionariosHotel)):
    if FuncionariosHotel[i][3] > mediaSalario:
        funcionariosAcimaMedia.append(FuncionariosHotel[i][0])
print(f"Lista com o nome dos funcionários que ganham acima da média salarial da empresa: {funcionariosAcimaMedia}")
