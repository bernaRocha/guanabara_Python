distancia_viagem = float(input('Qual a distância da viagem em Km: '))
# valor_kilometro = int(input('Qual o valor por cada Kilometro'))


# if distancia_viagem <= 200:
#     preco = distancia_viagem * 0.5
# else:
#     preco = distancia_viagem * 0.75

preco = distancia_viagem * 0.5 if distancia_viagem <= 200 else distancia_viagem * 0.75

print(f'Sua viagem terá um custo de R${preco:.2f}')
