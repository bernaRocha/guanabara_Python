'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep
from os import system
system('clear')

def contador(inicio, fim, indice):
    print(f'Contagem de {inicio} até o {fim} de {indice} em {indice}:')
    sleep(2.0)

    if indice < 0:
        indice *= -1
    if indice == 0:
        indice == 1


    if inicio < fim:
        contador = inicio
        while contador <= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(0.3)
            contador += indice
        print('FIM!')
    else:
        contador = inicio
        while contador >= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador -= indice
        print('FIM!')


contador(1, 10, 1)
contador(10,0 ,2)
print('-=' * 20)

print('Contagem personalizada ')
inicio = int(input('Qual o início? '))
fim = int(input('Qual o fim?       '))
indice = int(input('Qual o índice? '))

contador(inicio, fim, indice)
