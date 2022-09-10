from math import radians
from os import system
from random import randint
system('clear')

computador = randint(0, 10)
print('Pensei em um número entre 0 e 10'
'Consegue adivinhar????')

acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('qual o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou == True
    else:
        if jogador < computador:
            print('Menor do que o número pensado...tente de novo')
        elif jogador > computador:
            print('Maior do que o número pensado....tente novamente')
print(f'Acertou com {tentativas} palpites, parabéns!!!')

