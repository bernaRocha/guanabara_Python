from os import system

system('clear')

peso_atual = float(input('Qual seu peso atual em Kg: '))
altura = float(input('Qual a sua altura: '))

imc = peso_atual / (altura * altura)

muito_abaixo = imc < 17
abaixo_peso = imc <= 18.5
peso_normal = imc <= 25
sobrepeso = imc <= 30
obesidade_grau1 = imc <= 35
obesidade_grau2 = imc <= 40
obesidade_morbida = imc > 40

print(f'Seu IMC é de {imc:.1f}')

if muito_abaixo:
    print(f'Seu IMC é {imc}. Seu peso está muito baixo!')
elif abaixo_peso:
    print(f'Seu IMC é {imc}. Você está abaixo do peso')
elif peso_normal:
    print(f'Seu IMC é {imc}. Você está com o peso normal')
elif sobrepeso:
    print(f'Seu IMC é {imc}. Você está com sobrepeso')
elif obesidade_grau1:
    print(f'Seu IMC é {imc}. Você está com obesidade grau 1, cuidado')
elif obesidade_grau2:
    print(f'Seu IMC é {imc}. Você está com obesidade grau 2, cuidado')
else:
    print(f'Seu IMC é {imc}. Você está com obesidade mórbida, cuidado')
    