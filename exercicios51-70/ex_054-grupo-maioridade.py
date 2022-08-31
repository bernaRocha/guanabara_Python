from os import system
from datetime import date
system('clear')

ano_atual = date.today().year

total_maior = 0
total_menor = 0

for pessoa in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoa} pessoa nasceu: '))
    idade = ano_atual - nascimento
    if idade >= 21:
        total_maior += 1
   
    else:
        total_menor += 1
        
print(f'Temos um total de {total_maior} pessoas maiores de idade.')
print(f'Temos um total de {total_menor} pessoas menores de idade')
