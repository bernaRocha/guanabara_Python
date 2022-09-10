from os import system
from random import choice

system('clear') # Limpa a tela 

aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(lista)

print(f'O aluno escolhido é {escolhido}')
