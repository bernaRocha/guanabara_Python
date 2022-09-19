'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
e fechados na ordem correta.
'''

from os import system
system('clear')

expressao = input('Digite a expressão matemática: ')
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

valido = len(pilha) == 0

if valido:
    print(f'A expressão {expressao} é válida!')
else:
    print(f'A expressão {expressao} NÃO é válida!')
