'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep
from os import system
system('clear')

def maior(*numeros):
    contador = maior = 0
    print('\nAnalisando os valores passados....')
    for valor in numeros:
        print(f'{valor} ',end='', flush=True)
        sleep(0.3)

        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'\nForam informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 4, 6, 7, 8, 3, 4, 5, 2, 46)
maior(0)
maior(1, 67, 234, 456)
