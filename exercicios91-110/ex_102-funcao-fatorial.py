'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''
from os import system
system('clear')

def fatorial(numero, show=False):
    '''
    Calcula o fatorial de um número.
    :parâmetro numero: o número a ser calculado o seu fatorial
    :parâmetro show(opcional) mostra ou não a conta
    :return: Retorna o fatorial de um número
    '''
    fatorial = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        
        fatorial *= c
    return fatorial


print(fatorial(7))
print(fatorial(7, show=True))
