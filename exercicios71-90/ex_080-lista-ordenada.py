'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.
'''
from os import system
system('clear')

lista = []
for c in range(0, 5):
    numero = int(input('Registre um valor: '))

    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1

print(f'Os valores registrados são: {lista}')
