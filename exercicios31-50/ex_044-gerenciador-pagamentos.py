from os import system
from time import sleep

system('clear')

print('============LOJAS ROCHA============')
sleep(1)

preco = float(input('Valor das compras: '))

print('''  Formas de pagamento
[ 1 ] à vista em dinheiro / PIX (desconto de 10%)
[ 2 ] à vista no cartão de crédito (desconto de 5%)
[ 3 ] 2x no cartão - sem desconto
[ 4 ] 3x ou mais no cartão com juros ''', end="\n\n")

opcao = int(input('Qual a opção desejada? '))

opcao1 = preco - (preco * 0.1)
opcao2 = preco - (preco * 0.05)
opcao3 = preco
opcao4 = preco + (preco * 0.2)

if opcao == 1:
    preco = opcao1
    print(f'Sua compra de R${preco} com 10% de desconto terá um total a pagar de R${preco:.2f}')
elif opcao == 2:
    preco = opcao2
    print(f'Sua compra de R${preco} com 5% de desconto terá um total a pagar de R${preco:.2f}')
elif opcao == 3:
    preco = opcao3
    parcela = preco / 2
    print(f'O total a pagar é de R${preco:.2f} e cada parcela será de R${parcela:.2f}')
elif opcao == 4:
    preco = opcao4
    total_parcelas = int(input('Quantas pacelas? ', end="\n\n"))
    parcela = preco / total_parcelas
    print(f'O total a pagar é de R${preco:.2f} e cada parcela é de R${parcela:.2f}')
else:
    print('Opção inválida, tente novamente')
