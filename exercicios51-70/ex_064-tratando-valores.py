from os import system
system('clear')

numero = contador = soma = 0
numero = int(input('Digite um número [999 para encerrar]: '))

while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [999 para encerrar]: '))

print(f'Você digitou {contador} números e a soma deles é {soma}')