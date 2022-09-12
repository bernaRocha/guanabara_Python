from os import system
system('clear')

contagem = soma = 0

while True:
    numeros = int(input('Digite um valor (999 para parar): '))
    if numeros == 999:
        break
    soma += numeros
    contagem += 1
print(f'A soma dos {contagem} valores é {soma}')
print('Fim do programa')
