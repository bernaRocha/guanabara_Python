'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário 
possa mostrar as notas de cada aluno individualmente.
'''
from os import system
system('clear')

ficha = list()

while True:
    nome = input('Registre o nome do aluno: ')
    nota_1 = float(input('Nota 1 do aluno: '))
    nota_2 = float(input('Nota 2 do aluno: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resposta in 'N':
        break
print('-'*30)
print(f'{"No.":<}{"Nome":<10}{"Média":>8}')
print('-'*30)

for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-'*30)
    opcao = int(input('Deseja ver as notas de qual aluno? (9999 interrompe) '))
    if opcao == 9999:
        print('FINALIZANDO O PROGRAMA')
        break

    if opcao <= len(ficha) -1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('<<< AO SEU DISPOR >>>')
