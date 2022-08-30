from os import system

system('clear')

numero = int(input('Digite um número: '))
total = 0 # total de divisões

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {numero} foi divisível {total} vezes')

if total == 2:
    print('E por isso ele é um número PRIMO')
else:
    print('Não é um número primo')
print(' -> FIM')
