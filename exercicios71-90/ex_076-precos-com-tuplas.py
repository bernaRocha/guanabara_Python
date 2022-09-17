'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
from os import system
system('clear')

# tupla
listagem = ('Kindle', 399.05,
            'Livro Python', 104.90,
            'Pense em Python', 75.90,
            'TDD com Python', 67.50,
            'Linguagem C', 65.80,
            'Arquitetura de redes', 97.80)

print(f'{"LISTA DE PREÇOS":^40}')
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>7.2f}')
    