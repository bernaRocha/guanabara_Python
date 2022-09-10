"""
tempo = int(input("Quantos anos tem seu carro: "))
print(f'Carro novo' if tempo <= 3 else 'Carro velho')
print('-----FIM-----')

"""
from os import system
from random import randint
from time import sleep
system('clear')

computador = randint(0, 100)

print('-=-' * 26)
print()
print('Vou pensar em um número entre 0 e 100. Tente adivinhar....')
print()
print('-=-' * 26)

jogador = int(input("Qual número eu pensei? "))
print('PROCESSANDO...')

sleep(3)
system('clear')

venceu = jogador == computador

if venceu:
    print('Você venceu')
else:
    print('Pensei em outro número, tente novamente.')

