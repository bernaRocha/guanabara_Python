'''
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
from os import system
system('clear')

pessoas = list()
pessoa = dict()

soma_idade = media_idade = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').capitalize()
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.') 
    pessoa['idade'] = int(input('Idade: '))

    soma_idade += pessoa['idade']

    pessoas.append(pessoa.copy()) 
    #### a lista de pessoas recebe uma cópia do dicionário pessoa
    while True:
        resposta = input('Quer continuar? [S/N] ').upper()[0] 
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-' * 20)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')

media_idade = soma_idade / len(pessoas)
print(f'A média de idades é de {media_idade:5.2f} anos.')
print(f'As mulheres cadastradas foram ',end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in pessoas:
    if p["idade"] >= media_idade:
        print('          ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< FIM >>')
