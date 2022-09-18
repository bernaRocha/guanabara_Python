
'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''
from os import system
system('clear')

lista_numeros = []

maior = menor = 0

limite = int(input('Quantos números deseja registrar na lista: '))
for numero in range(0, limite):
    lista_numeros.append(int(input(f'Registre um número na posição {numero + 1}: ')))
    if numero == 0:
        maior = menor = lista_numeros[numero]
    else:
        if lista_numeros[numero] > maior:
            maior = lista_numeros[numero]
        if lista_numeros[numero] < menor:
            menor = lista_numeros[numero]
print(':' * 30)
print(f'Você digitou os valores: {lista_numeros}')
print(f'O menor valor digitado foi: {menor} nas posições ', end='')
for i, valores in enumerate(lista_numeros):
    if valores == menor:
        print(f'{i + 1}...', end='') 
print()
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, valores in enumerate(lista_numeros):
    if valores == maior:
        print(f'{i + 1}...', end='') 
print()
