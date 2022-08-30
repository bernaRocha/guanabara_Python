from os import system

system('clear')

# numero = int(input('A tabuada de qual número desejar ver: '))

# for c in range(1, 11):
#     resultado = numero * c
#     print(f'{numero} X {c} = {resultado}')


multiplicando = int(input('Qual o multiplicando da operação: '))
multiplicador = int(input('A partir de qual número deseja multiplicar: '))

for multiplicando in range(multiplicando, multiplicador):
    resultado = multiplicando * multiplicador
    print(f'{multiplicando} X {multiplicador} = {resultado}')
