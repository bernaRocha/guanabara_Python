'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''

from os import system
system('clear')

custo_acima_1000 = total_gastos = produto_mais_barato = contador = 0
barato = ' '
while True:
    produto = input('O que está comprando: ')
    preco = float(input('Preço do produto R$ '))
    contador += 1
    total_gastos += preco

    if preco > 1000:
        custo_acima_1000 += 1

    if contador == 1 or preco < produto_mais_barato:
        produto_mais_barato = preco
        barato = produto_mais_barato
    # else:
    #     if preco < produto_mais_barato:
    #         produto_mais_barato = preco
    #         barato = produto_mais_barato

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
    
print(f'-------- FIM DO PROGRAMA --------')
print(f'O total da compra foi R${total_gastos:.2f}')
print(f'Temos {custo_acima_1000} produtos acima de 1.000 reais.')
print(f'O produto mais barato foi {barato} e custou {produto_mais_barato:.2f} reais')
