from os import system
system('clear')

sexo = input('Informe seu sexo: [M/F]: ').strip().upper()[0]
#idade = int(input('Informe seu idade: '))

while sexo not in 'MF':
    sexo = input('Dados inválidos. Informe seu sexo: [M/F] ').strip().upper()[0]

print(f'Registrado com sucesso, sexo: {sexo}.')
