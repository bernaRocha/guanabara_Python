from os import system
system('clear')

salario = float(input('Qual é o salário atual do funcionário? '))

if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.1)

print(f'O novo salário do funcionário de {salario:.2f} foi alterado para {novo_salario:.2f}')
