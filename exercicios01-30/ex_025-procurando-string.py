from os import system
system('clear')

nome = input("Qual seu nome completo? ").strip()

tem_silva = ('Silva' in nome.lower())

print(f'Seu nome é {nome}')
print(f'Seu nome tem Sila? {tem_silva}')
