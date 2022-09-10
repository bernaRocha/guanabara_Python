from os import system
system('clear')

numero = int(input('Digite um número para o cálculo do Fatorial: '))
c = numero
fatorial = 1

print(f'Calculando {numero}! = ')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(f'{fatorial}')
