## Verificações
from os import system
system('clear')

algo = input("Digite algo: ")

print(f'O tipo primitido do que foi digitado é {type(algo)}')
print(f'O que foi digitado é um numeral? {algo.isnumeric()}')
print(f'Há espaços? {algo.isspace()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')
