from os import system

system('clear')

#### Resolução mais verbosa

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Peso da pessoa ({p}): '))
    if p == 1:
        maior = peso # O primeiro peso liso será sempre maior e menor ao mesmo tempo
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
