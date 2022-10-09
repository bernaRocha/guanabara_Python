'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
'''
from os import system
system('clear')

def escreva(mensagem):
    tamanho = len(mensagem) + 4
    
    print('~' * tamanho)
    print(f'  {mensagem}')
    print('~' * tamanho)

escreva('Oi')
escreva('Quero dormir')
