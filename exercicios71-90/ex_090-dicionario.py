'''
Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. No final, 
mostre o conteúdo da estrutura na tela.
'''
from os import system
system('clear')

aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for chave, valor in aluno.items():
    print(f'   - {chave} é igual a {valor}')