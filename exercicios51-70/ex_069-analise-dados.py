'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''

from os import system
system('clear')

total_homens = total_maior_18 = total_mulheres_menos_20 = 0

while True:
    idade = int(input('Qual a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F]: ').strip().upper()[0]
    
    # Verificações
    if idade >= 18:
        total_maior_18 += 1

    if sexo == 'M':
        total_homens += 1
    
    if sexo == 'F' and idade < 20:
        total_mulheres_menos_20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break

print(f'O total de pessoas maiores de 18 é: {total_maior_18}')
print(f'O total de homens cadastrados é: {total_homens}')
print(f'O total de mulheres menores de 20 anos é: {total_mulheres_menos_20}')
print('Acabou!!!')
