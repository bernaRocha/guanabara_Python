from os import system

system('clear')

soma = 0
contador = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
        #print(c, end=' ')
print(f'A soma dos valores solicitados é {soma}, foram contados {contador} valores')

##### Feito de forma mais complexa

inicio_contagem = int(input('A partir de quanto deseja contar? '))
fim_contagem = int(input('Até quanto desejar a contagem? '))
indice = int(input('Qual o índice da contagem? '))
multiplo = int(input('Números múltiplos de qual número: '))

for a in range(inicio_contagem, fim_contagem, indice):
    if a % multiplo == 0:
        contador += 1
        soma += a
        print(a, end=' ')
        print('')
print(f'A soma dos valores solicitados é {soma}, foram contados {contador} valores')
    