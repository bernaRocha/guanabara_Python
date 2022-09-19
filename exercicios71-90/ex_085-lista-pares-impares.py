'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
'''
from os import system
system('clear')

lista_numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Registre o {c}º valor: '))
    
    par = valor % 2 == 0 
    
    if par:
        lista_numeros[0].append(valor)
    else:
        lista_numeros[1].append(valor)

#ordenando as listas
lista_numeros[0].sort()
lista_numeros[1].sort()

print(f'Os valores pares digitados fora: {lista_numeros[0]}')
print(f'Os valores ímpares digitados fora: {lista_numeros[1]}')
