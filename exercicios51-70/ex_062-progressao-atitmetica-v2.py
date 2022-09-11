from os import system
system('clear')

primeiro_termo = int(input('Defina o primeiro termo da PA: '))
razao = int(input('Defina a razão da PA: '))

termo = primeiro_termo
contador = 1
total = 0
adicional = 10

while adicional != 0:
    total += adicional
    while contador <= total:
        print(f'{termo} ', end='')
        termo += razao
        contador += 1
    print('PAUSA')

    adicional = int(input('Quantos termos deseja mostrar mais? '))
    print(f'Progressão finalziada com {total} termos mostrados.')
print('FIM')
