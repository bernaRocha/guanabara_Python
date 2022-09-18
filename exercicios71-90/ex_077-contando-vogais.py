'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
from os import system
system('clear')

# cada palavra é uma lista de letras
palavras = ('cansado', 'estudando', 'frio', 'saudades',
'github', 'concurso', 'debate', 'palavra', 'amizade', 'felinos', 
'lista', 'tupla', 'vetores', 'matrizes')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=" ")
