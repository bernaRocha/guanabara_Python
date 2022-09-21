'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
'''
from os import system
from random import randint
from time import sleep
system('clear')

lista = list() # É feito uma cópia da lista
jogos = list()
print('-'*30)
print('      JOGA NA MEGA SENA          ')
print('-'*30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1

while total <= quantidade:
    contagem = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero) # adiciona o numero na lista
            contagem += 1
        if contagem >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-' * 3, f'  SORTEANDO {quantidade} JOGOS  ', '-' * 3)

for indice, lista_jogos in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista_jogos}')
    sleep(1)

print('-' * 5, f'  BOA SORTE  ', '-' * 5)
