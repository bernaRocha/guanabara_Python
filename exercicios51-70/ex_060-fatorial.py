from os import system
from math import factorial
system('clear')

numero = int(input('Digite um número para o cálculo do Fatorial: '))
fatorial = factorial(numero)
print(f'O fatorial de {numero} é {fatorial}')
