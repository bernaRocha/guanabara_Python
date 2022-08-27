from os import system


nome_inteiro = input('Digite seu nome completo: ').strip()
nome_separado = nome_inteiro.split()

primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[-1]

print('Prazer em te conhecer')
system('clear')
print(f"Seu nome completo é {nome_inteiro}")
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')
