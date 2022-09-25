'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno 
retangular (largura e comprimento) e mostre a área do terreno.
'''
from os import system
system('clear')

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno de {largura} m de largura\n'
    f'e {comprimento} m de comprimento é {area} m² ')

print(' Controle de terrenos')
print('-' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
