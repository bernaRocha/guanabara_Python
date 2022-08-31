#### Programa para verificar se determinada frase é palíndromo
#### Há duas soluções, com laço for e com fatiamento
###
### Exemplos de palíndromos:  apos a sopa || a sacada da casa 
### a torre da derrota || o lobo ama o bolo || anotaram a data da maratona 
from os import system

system('clear')

frase = input('Digite uma frase [não use acentos]: ').strip().upper()
palavras = frase.split() # Gera uma lista/ vetor
junto = ''.join(palavras) # Juntou a lista para eliminar os espaços
# inverso = '' 
inverso = junto[::-1]

'''for letra in range(len(junto) - 1, -1, -1): # Laço for para inverter o que foi escrito
    inverso += junto[letra]'''

print(f'O inverso de {junto} é {inverso}') 

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
