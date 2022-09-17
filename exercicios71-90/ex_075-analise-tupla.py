'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
from os import system
system('clear')

numeros = (int(input('Registre um número: ')),
          int(input('Registre outro número: ')),
          int(input('Registre mais um número: ')),
          int(input('Registre o último número: ')))

print(f'Você registrou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 aparececu na posição {numeros.index(3)+1}.')
else:
    print('O valor 3 não foi digitado.')
for verifica_par in numeros:
    if verifica_par % 2 == 0:
        print(f'Os valores pares são: {verifica_par}')
