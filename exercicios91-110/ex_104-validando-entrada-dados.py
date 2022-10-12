'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico.
'''
from os import system
system('clear')

def leiaInt(mensagem):
    ok = False
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido')
        if ok:
            break
    return valor
    
numero = leiaInt('Digite um número: ')
print(f'Você digitou o número {numero}')
