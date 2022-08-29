from os import system
from random import randint
from time import sleep

system('clear')

itens = ('Pedra', 'Papel', 'Tesoura')
jogada_computador = randint(0, 2)

print(''' Suas opções: 
        [ 0 ] Pedra
        [ 1 ] Papel
        [ 2 ] Tesoura
''')

jogador = int(input('Qual a sua jogada? '))
print('', end='\n\n')

print('     JO')
sleep(0.5)
print('     KEN')
sleep(0.5)
print('     PO!!!')
sleep(0.5)

print('', end='\n\n')

print(' -=' * 11)
print(f'    Computador jogou {itens[jogada_computador]}')
print(f'     Jogador jogou {itens[jogador]}')
print(' -=' * 11)

if jogada_computador == 0: # pedra
    if jogador == 0:
        print('Deu empate, tente novamente')
    elif jogador == 1:
        print('  Você ganhou')
    elif jogador == 2:
        print(' Computador ganhou')
    else:
        print('Jogada inválida')

if jogada_computador == 1: # Papel
    if jogador == 0:
        print(' Computador ganhou')
    elif jogador == 1:
        print('Deu empate, tente novamente')
    elif jogador == 2:
        print('  Você ganhou')
    else:
        print('Jogada inválida')


if jogada_computador == 2: # Tesoura
    if jogador == 0:
        print('  Você ganhou')
    elif jogador == 1:
        print(' Computador ganhou')
    elif jogador == 2:
        print('Deu empate, tente novamente')
    else:
        print('Jogada inválida')

