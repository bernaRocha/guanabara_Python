from os import system
system('clear')

primeiro_termo = int(input('Defina o primeiro termo da PA: '))
razao = int(input('Defina a razão da PA: '))

termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f'{termo} ', end='')
    termo += razao
    contador += 1
print('FIM')
