'''
Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.

É uma protovalidação
'''
from os import system
system('clear')

def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')

if gols.isnumeric():
    gols = int(gols)
if nome.strip() == '':
    ficha()
else:
    ficha()