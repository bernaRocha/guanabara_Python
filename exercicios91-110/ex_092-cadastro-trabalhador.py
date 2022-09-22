'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime
from os import system
system('clear')

trabalhador = dict()
trabalhador['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - nascimento
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratacao']))

for chave, valor in trabalhador.items():
    print(f'  - {chave} tem o valor de {valor}')
