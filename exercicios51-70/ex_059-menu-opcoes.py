from os import system
from time import sleep
system('clear')

numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))
print('-=' * 10)
opcao = 0

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
if numero1 > numero2:
    maior = numero1
else:
    maior = numero2

while opcao != 6:
    print('')
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Subtrair
[ 4 ] Maior
[ 5 ] Novos números
[ 6 ] Sair do programa ''')
    print('')
    opcao = int(input('>>>> Qual a opção desejada? '))
    print('')
    
    if opcao == 1:
        print(f'A soma de {numero1} + {numero2} é {soma}')
    elif opcao == 2:
        print(f'A multiplicação de {numero1} pelo {numero2} é {multiplicacao}')
    elif opcao == 3:
        print(f'A subtração de {numero1} pelo {numero2} é {subtracao}')
    elif opcao == 4:
        print(f'Entre {numero1} e {numero2} o {maior} é o maior')
    elif opcao == 5:
        print('Informe os números novamente')
        numero1 = int(input('Primeiro valor: '))
        numero2 = int(input('Segundo valor: '))
    elif opcao == 6:
        sleep(2)
        print('Finalizando o programa...........')
    else:
        print('Opção inválida, tente novamente')
        sleep(2)
