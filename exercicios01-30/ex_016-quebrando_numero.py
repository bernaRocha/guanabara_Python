from os import system
from math import trunc
system('clear')

numero = float(input("Digite um valor: "))
print(f"O número digita foi {numero} e sua parte inteira é {trunc(numero)}")

###### Sem importação de módulo

## Converte float para int

numero = float(input("Digite um valor: "))
print(f"O número digita foi {numero} e sua parte inteira é {int(numero)}") 
