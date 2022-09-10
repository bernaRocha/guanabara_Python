from os import system
system('clear')

frase = input('Digite uma frase: ').strip().upper()

letra = input('Qual letra você deseja contar ? ')
ocorrencias = frase.count(letra.upper())
posicao_1 = (frase.lower().find(letra) + 1)
posicao_final = frase.lower().rfind(letra) + 1

print(f'A letra "{letra}" aparece {ocorrencias} vezes na frase.')
print(f'A primeira da letra {letra} apareceu na posição {posicao_1}')
print(f'A útlima posição de {letra} na frase é na posição {posicao_final}')
