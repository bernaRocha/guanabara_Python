from os import system

system('clear')

print('Analisando as medidas...')
reta_1 = float(input('Primeiro seguimento: '))
reta_2 = float(input('Segundo segmento: '))
reta_3 = float(input('Terceiro segmento: '))

equilatero = reta_1 == reta_2 == reta_3
isosceles = reta_1 == reta_2 or reta_2 == reta_3 or reta_1 == reta_3
escaleno = reta_1 != reta_2 != reta_3

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_2 + reta_1:
    print('Os segmentos podem formar um triângulo')

    if equilatero:
        print('É um triângulo equilatero')
    elif isosceles:
        print('É um triângulo isósceles')
    else:
        print('É um triângulo escaleno')

else:
    ('Os segmentos NÃO podem formar um triângulo')
