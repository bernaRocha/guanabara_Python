'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''
from os import system
system('clear')

brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

#for times in brasileirao:
#    print(times)

print('-=' * 15)
print(f'Lista de times: {brasileirao}')
print('-=' * 15)

print(f'Os cinco primeiros times são {brasileirao[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos são {brasileirao[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-=' * 15)
print(f'A posição do Chapecoense é: {brasileirao.index("Chapecoense")+ 1}')
