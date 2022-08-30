from os import system

system('clear')

numeros = []
somatorio = 0
contador = 0

for n in range(1, 7):
    numero = int(input(f'{n} - Registre um número: '))

    if numero % 2 == 0:
        somatorio += numero
        contador += 1

    numeros.append(numero)

print('')
print(f'Você registrou {contador} números pares, a soma deles é {somatorio}', end='\n\n')
print(f'Números registrados: {numeros}')
