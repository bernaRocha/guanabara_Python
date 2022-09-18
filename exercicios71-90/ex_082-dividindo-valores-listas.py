'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares 
e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
'''
from os import system
system('clear')

numeros = list()
pares = list()
impares = list()

while True:
    numeros.append(int(input('Registre um número: ')))
    resposta = input('Quer continuar? [S/N] ').strip().upper()
    if resposta in 'N':
        break

for indice, valores in enumerate(numeros):
    if valores % 2 == 0:
        pares.append(valores)
    elif valores % 2 == 1:
        impares.append(valores)

print(f'\nOs números registrados são: {numeros}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
