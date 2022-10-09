'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
from os import system
system('clear')

def voto(ano):
    from datetime import date #### importado dentro da função para economizar memória
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

ano_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_nascimento))
