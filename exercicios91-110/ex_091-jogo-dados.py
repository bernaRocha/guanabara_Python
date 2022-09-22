'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.
'''
from os import system
from random import randint
from time import sleep
from operator import itemgetter
system('clear')

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

#ranking = dict()
ranking = list()

print('Valores sorteados:')
for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('>' * 30)
print('  == RANKING == ')
for indice, valor in enumerate(ranking):
    print(f'{indice + 1}º lugar: {valor[0]} com {valor[1]}')
    sleep(1)
