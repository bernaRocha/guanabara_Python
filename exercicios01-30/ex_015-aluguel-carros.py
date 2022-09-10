"""
Cálculo do valor a ser pago pelo aluguel de um carro.
Levemente modificado do vídeo da aula.
"""
from os import system
system('clear')

dias_alugados = int(input("Por quantos dias o c arro foi usado: "))
kilometros_usados = float(input("Quantos kilometros rodados: "))
valor_dia = float(input("Qual o valor da diária do carro: "))
taxa_uso = 50

custo_total = valor_dia * (kilometros_usados * 0.15 ) * dias_alugados + taxa_uso

print(f"O total a ser pago é R${custo_total:.f}")
