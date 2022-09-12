from os import system
system('clear')

continuar = 'S'

soma = quantidade = media = 0
maior = menor = 0

while continuar in 'Ss':
    numeros = int(input('Digite um número: '))
    soma += numeros
    quantidade += 1

    if quantidade == 1:
        maior = menor = numeros # tendo só um número ele será o menor e o maior
    else:
        if numeros > maior: # se o número foi maior que o maior que no momento é o primeiro número, então maior recebe o número
            maior = numeros
        if numeros < menor: # se o número for menor que o menor que no momento é o primeiro número, então menor recebe o número
            menor = numeros

    continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    
media = soma / quantidade
print(f'Você digitou {quantidade} números e a média deles é {media:.2f}')
print(f'O maior número é {maior} e o menor é {menor}')
print('Fim do programa')
