from os import system
system('clear')

print('Sequência de Fibonacci')
termos = int(input('Quantos termos deseja mostrar? '))
termo_1 = 0
termo_2 = 1

print(f'{termo_1} -> {termo_2}', end="")
contador = 3
while contador <= termos:
    termo_3 = termo_1 + termo_2
    print(f' -> {termo_3}', end="")
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1

print(' >> FIM')
