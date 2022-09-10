from os import system
from datetime import date

system('clear')

ano_atual = date.today().year
ano_nascimento = int(input('Qual o ano de nascimento: '))
idade = ano_atual - ano_nascimento

fez_aniversario = input('Já fez aniversário esse ano? [Sim][sim]/[Não][não] ')

##### Verifica idade
if fez_aniversario == "Sim" or "sim":
    idade = ano_atual - ano_nascimento 
    print(f'Quem nasceu em {ano_nascimento} e fez aniversário tem {idade} anos.')
else:
   idade = ano_atual - ano_nascimento - 1
   print(f'Quem nasceu em {ano_nascimento} e não fez aniversário tem {idade} anos.')

print(f"O atleta tem {idade} anos.")

##### Classificação quanto a idade
if idade <= 9:
    print('Classificação MIRIM')
elif idade <= 14:
    print('Classificação INFANTIL')
elif idade <= 19:
    print('Classificação JÚNIOR')
elif idade <= 25:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')
    