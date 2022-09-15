'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados 
e também indique o menor e o maior valor que estão na tupla.
'''
from os import system
from random import sample
system('clear')

quantidade = int(input('Quantos números deseja sortear? '))
numeros = tuple(sample(range(60), quantidade))

NUMEROS_ORDENADOS = sorted(numeros)
MAXIMO_VALOR = max(numeros)
MINIMO_VALOR = min(numeros)

print(f'\nOs números sorteados são {numeros}')
print(f'\nEm ordem fica: {NUMEROS_ORDENADOS}')
print(f'\nO maior valor é {MAXIMO_VALOR} e o menor valor é {MINIMO_VALOR}')
