'''
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
'''
from os import system
system('clear')

matriz = [[0, 0 , 0], [0, 0 , 0], [0, 0 , 0]] # para não usar o append
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Registre o valor para [{linha}, {coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
