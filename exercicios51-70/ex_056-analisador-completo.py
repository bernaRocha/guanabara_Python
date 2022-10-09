from os import system

system('clear')

somatorio_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
mulher_abaixo_20 = 0

for p in range(1, 5):
    print(f'---- PESSOA ({p}) ----')
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Diga sua idade: '))
    sexo = input('Diga seu sexo [M/F]: ').strip()

    somatorio_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome

    if sexo in 'Ff' and idade < 20:
        mulher_abaixo_20 += 1

media_idade = somatorio_idade / 4
print(f'A média de idades desse grupo é de {media_idade:.1f} anos.')
print(f'O homem mais velho se chama {nome_mais_velho} e tem {maior_idade_homem} anos de idade.')
print(f'Ao todo são {mulher_abaixo_20} mulheres abaixo de 20 anos.')
