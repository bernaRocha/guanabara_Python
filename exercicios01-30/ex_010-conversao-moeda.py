"""
Exercício Python 010: 
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
e mostre quantos dólares ela pode comprar.
"""

from os import system
system('clear')

cotacao_dolar = float(input("Qual o valor do dólar hoje: US$ "))
valor_carteira = float(input("Quanto reais deseja converter: R$ "))

valor_convertido = valor_carteira / cotacao_dolar

print(f"Com a quantia de {valor_carteira}R$ você pode comprar {valor_convertido:.2f} dólares. Cotação do dia {cotacao_dolar}")
