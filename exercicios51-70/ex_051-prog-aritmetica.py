# Script de progressão airtmética
#   a variável fim é para declarar o fim da PA, para ser usada tem que descomentar e alterar no laço for
#   a variável decimo é para que seja impresso exatos 10 termos da PA
#   GitHub: @bernaRocha

from os import system

system('clear')

primeiro = int(input('Primeiro termo: '))
# fim = int(input('Fim da PA: '))
razao = int(input('Razão da PA: '))
decimo = primeiro + (9) * razao

for c in range(primeiro, decimo + razao, razao):
    print(f'{c} ', end=' -> ')
print('FIM')
