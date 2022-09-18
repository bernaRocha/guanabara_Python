'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. || **  Item alterado por decisão minha **
'''
from os import system
system('clear')

valores = []
while True:
    valores.append(int(input('Registre um valor: ')))
    resposta = input('Quer continuar? [S/N] ').strip().upper()
    if resposta in 'N':
        break

print(f'Foram registrados {len(valores)} elementos')
print(f'Os valores registrados são: {valores}')

valores.sort(reverse=True)
ao_contrario = valores
print(f'Em ordem decrescente são {ao_contrario}')

valor_especifico = int(input('Qual valor em específico deseja verificar: '))
if valor_especifico in valores:
    print(f"O valor {valor_especifico} faz parte da lista")
else:
    print(f"O valor {valor_especifico} NÃO faz parte da lista")
