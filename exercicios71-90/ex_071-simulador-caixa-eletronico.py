'''
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa 
vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$100, R$50, R$20, R$10 e R$1.
'''

from os import system
system('clear')

print('=' * 30)
print('{:^30}'.format('Banco Seu dinheiro é lindo'))
print('=' * 30)

valor = int(input('Quanto deseja sacar? R$ '))
total = valor
cedula = 100
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else: 
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R$ {cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre')
