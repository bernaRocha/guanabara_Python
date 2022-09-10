from os import system
system('clear')

casa = float(input('Qual o valor da casa: R$ '))
salario = float(input("Qual o salário do comprador: R$ "))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 0.30

print(f'Para pagar uma casa de R${casa} em {anos} anos'
f'a prestação será de R${prestacao}')

if prestacao <= minimo:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo negado')
    