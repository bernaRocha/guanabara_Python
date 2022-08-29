from os import system

system('clear')

for n in range(2, 51, 2): # De 2 até 51 pulando de dois em dois
    if n % 2 == 0: 
        print(n, end=" ")
print('Fim')

#### Com a participação do usuário

inicio_sequencia = int(input('Qual o início da sequência: '))
fim_sequencia = int(input('Qual o fim da sequência: '))
indice = int(input('Qual o índice da sequência: '))

for n in range(inicio_sequencia, fim_sequencia, indice):
    print(n, end=" ")
print('FIM')
