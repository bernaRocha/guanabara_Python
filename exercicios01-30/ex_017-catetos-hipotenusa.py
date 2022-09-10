"""
ler o comprimento do cateto oposto e do adjacente
de um triângulo retângulo, calcule e mostre o comprimento
da hipotenusa
"""
from os import system
from math import hypot
system('clear')

#### Uma forma de resolver

cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")

#### Outra forma

hipotenusa = hypot(cateto_oposto, cateto_adjacente)
