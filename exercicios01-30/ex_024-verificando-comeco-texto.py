"""
Um programa que leia um nome e retorne se começa ou não com "Santo"
"""
from os import system
system('clear')

cidade = input("Digite o nome da cidade: ").strip()

print(cidade[0:5].upper() == 'SANTO') 
