'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, 
serão exibidos todos os valores únicos digitados, em ordem crescente. 
'''

from os import system
system('clear')

numeros = list()

while True:
    n = int(input('Registre um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor registrado com sucesso')
    else:
        print('Valor repetido não será registrado')
    resposta = input('Deseja continuar? [S/N] ').strip().upper()
    if resposta in 'N':
        break
    
print('=+'*30)
print(f'Você digitou os valores: {numeros}')
numeros.sort()
print(f'Em ordem crescente fica: {numeros}')
