'''
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
from os import system
system('clear')

matriz = [[0, 0 , 0], [0, 0 , 0], [0, 0 , 0]] # para não usar o append
soma_par = soma_coluna_3 = maior_valor_linha_2 = 0

#preenche matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Registre o valor para [{linha}, {coluna}]: '))

# printa a matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 ==0:
            soma_par += matriz[linha][coluna]
    print()

print(f'A soma dos valores pares é {soma_par}')
for linha in range(0, 3):
    soma_coluna_3 += matriz[linha][2]
print(f'A soma dos valores da tericera coluna é {soma_coluna_3}')

for coluna in range(0, 3):
    if coluna == 0:
        maior_valor_linha_2 = matriz[1][coluna]
    elif matriz[1][coluna] > maior_valor_linha_2:
        maior_valor_linha_2 = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior_valor_linha_2} ')

