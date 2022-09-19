'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
from os import system
system('clear')

lista_temporaria = []
lista_principal = []
maior_peso = menor_peso = 0

while True:
    lista_temporaria.append(str(input('Registre o nome: ')))
    lista_temporaria.append(float(input('Registre o peso: ')))
    if len(lista_principal) == 0:
        maior_peso = menor_peso = lista_temporaria[1]
    else:
        if lista_temporaria[1] > maior_peso:
            maior_peso = lista_temporaria[1]
        if lista_temporaria[1] < menor_peso:
            menor_peso = lista_temporaria[1]
    
    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear()

    resposta = input('Deseja continuar? [S/N] ').strip().upper()

    if resposta == 'N':
        break

total_pessoas = len(lista_principal)
print('-=' * 30)
print(f'Ao total foram cadastradas {total_pessoas} pessoas')
print(f'O maior peso é de {maior_peso}Kg. Peso de ', end='')
for pessoa in lista_principal:
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}] ', end='')
print(f'O menor peso é de {menor_peso}Kg. Peso de ', end='')
for pessoa in lista_principal:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}] ', end='')
print()
print(f'Dados cadastrados: {lista_principal}')
