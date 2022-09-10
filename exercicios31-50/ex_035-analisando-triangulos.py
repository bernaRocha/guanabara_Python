from os import system
system('clear')

print('Analisando as medidas...')
reta_1 = float(input('Primeiro seguimento: '))
reta_2 = float(input('Segundo segmento: '))
reta_3 = float(input('Terceiro segmento: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_2 + reta_1:
    print('Os segmentos podem formar um triângulo')
else:
    ('Os segmentos NÃO podem formar um triângulo')
    