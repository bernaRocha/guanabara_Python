## Tipos primitivos int float bool str

# int = 7 -4 0 9134
# float = 4.7 0.0345
# bool = True False
# str = "Texto" 'texto' "0" "False"

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite o segundo: "))
soma = numero1 + numero2
print(f'A soma entre {numero1} e {numero2} é {soma}')

print(f'O tipo do número é {type(numero1)}')

algo = input("Digite algo ")
print(f'O que foi digitado é um número inteiro? {algo.isnumeric()}')
print(f'O que foi digitado é alfabético? {algo.isalpha()}')