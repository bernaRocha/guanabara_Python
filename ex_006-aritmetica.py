# antecessor, sucessor, dobro, triplo e raiz quadrada

numero = int(input("Digite o número: "))
antecessor = numero - 1
sucessor = numero + 1
dobro = 2 * numero
triplo = 3 * numero
raiz_quadrada = numero ** (1/2)

print(f"Analisando o número {numero}, seu antecessor é {antecessor} e o sucessor é {sucessor}")
print(f"O dobro de {numero} é {dobro} e o triplo é {triplo}")
print(f"A raiz quadra é {raiz_quadrada:.2f}")