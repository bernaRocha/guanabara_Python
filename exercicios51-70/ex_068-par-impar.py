from os import system
from random import randint
system('clear')

vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '

    while escolha not in 'PI':
        escolha = input('Par ou ímpar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
        print('Vamos jogar mais uma vez.....') 

print('-' * 26)
print(f'Fim do jogo! Você ganhou {vitoria} vezes.')  
