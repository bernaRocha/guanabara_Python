numero_1 = int(input('Primeiro número: '))
numero_2 = int(input('Segundo número: '))

if numero_1 > numero_2:
    print(f'{numero_1} é maior que {numero_2}')
elif numero_2 > numero_1:
    print(f'{numero_2} é maior que {numero_1}')
else:
    print(f'Os dois números são iguais')
    