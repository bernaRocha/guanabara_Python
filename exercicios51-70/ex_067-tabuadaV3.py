from os import system
system('clear')

while True:
    numero = int(input('Quer a tabuada de qual valor? '))
    print('_' * 10)
   
    if numero < 0:
        break

    for c in range(1,11):
        resultado = numero * c
        print(f'{numero} X {c} = {resultado}')
    print('_' * 10)

print('Fim do programa')
