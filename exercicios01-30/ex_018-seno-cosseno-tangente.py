"""
Ler um ângulo qualquer e mostrar:
seno, cosseno e tangente desse ângulo
"""
from os import system
from math import tan, cos, sin, radians
system('clear')

angulo = float(input("Digite o ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f"O seno do ângulo {angulo} é {seno:.2f}")
print(f"O cosseno do ângulo {angulo} é {cosseno:.2f}")
print(f"A tangente do ângulo {angulo} é {tangente:.2f}")
