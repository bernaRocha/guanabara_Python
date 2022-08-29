from datetime import date
from time import sleep
from os import system

system('clear')

ano_atual = date.today().year
nascimento = int(input('Seu ano de nascimento: '))
fez_aniversario = input('Já fez aniversário esse ano? [Sim][sim]/[Não][não] ')

if fez_aniversario == "Sim" or "sim":
    idade = ano_atual - nascimento 
    print(f'Quem nasceu em {nascimento} e fez aniversário tem {idade} anos em {ano_atual}.')
else:
   idade = ano_atual - nascimento - 1
   print(f'Quem nasceu em {nascimento} e não fez aniversário tem {idade} anos em {ano_atual}.')

sleep(2)

if idade == 18:
    print('Você tem que se alistar imediantamente.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você não tem 18 ainda, faltam {saldo} anos para o seu alistamento.')
    ano_alistamento = ano_atual + saldo
    print(f'Seu alistamento será em {ano_alistamento}')
elif idade > 18:
    saldo = idade - 18
    ano_alistamento = ano_atual - saldo
    print(f'Você deveria ter se alistado há {saldo} anos atrás.')
