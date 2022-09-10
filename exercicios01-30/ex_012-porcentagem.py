"""
Porcentagem com preço
"""
from os import system
system('clear')

preco = float(input("Qual o valor do produto? "))
desconto = float(input("Quanto de desconto tem esse produto? "))
com_desconto = preco - (preco * desconto / 100)
print(f"O produto de valor  R${preco} com o desconto de {desconto} % fica em R${com_desconto:.2f}")
