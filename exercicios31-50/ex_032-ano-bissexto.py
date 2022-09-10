from os import system
from datetime import date
system('clear')

ano = int(input("Qual ano quer analisar? Digite 0 para o ano atual: "))

if ano == 0:
    ano = date.today().year

# Fórmula do ano bissexto

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')
    