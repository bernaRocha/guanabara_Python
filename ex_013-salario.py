"""
Aumento de salário, uso de porcentagem
"""

salario = float(input("Qual o salário do funionário: "))
aumento = float(input("Quantos '%' de aumento ele terá: "))
salario_com_aumento = salario + (aumento/100 * salario)
print(f'O funcionário que tinha o salário de {salario} ganhou um aumento de {aumento}%, passará a ganhar R${salario_com_aumento}')