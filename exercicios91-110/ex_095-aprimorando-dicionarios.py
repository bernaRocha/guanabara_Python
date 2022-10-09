'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
from os import system
from time import sleep
system('clear')

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear() # limpa o dicionário jogador para a leitura de um novo
    jogador['nome'] = input('Nome do jogador: ')
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.append(jogador.copy())

    while True:
        resposta = input('Quer continuar? [S/N] ').upper()[0]
        if resposta in 'SN':
            break
        print('Responda apenas S ou N.')    
    if resposta == 'N':
        break

#### resultados    
print('*' * 30)
print('ID ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('*' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('*' * 30)

#### escolher dados a serem exibidos
while True:
    busca = int(input('Deseja ver os dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o ID {busca}')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('Encerrando o programa')
sleep(2)
print('<< Volte sempre >>')
