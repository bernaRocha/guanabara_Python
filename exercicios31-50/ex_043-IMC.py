from os import system
system('clear')

peso_atual = float(input('Qual seu peso atual em Kg: '))
altura = float(input('Qual a sua altura: '))

imc = peso_atual / (altura * altura)

MUITO_ABAIXO = imc < 17
ABAIXO_PESO = imc <= 18.5
PESO_NORMAL = imc <= 25
SOBREPESO = imc <= 30
OBESIDADE_GRAU1 = imc <= 35
OBESIDADE_GRAU2 = imc <= 40
OBESIDADE_MORBIDA = imc > 40

if MUITO_ABAIXO:
    print(f'Seu IMC é {imc:.2f}. Seu peso está muito baixo!')
elif ABAIXO_PESO:
    print(f'Seu IMC é {imc:.2f}. Você está abaixo do peso')
elif PESO_NORMAL:
    print(f'Seu IMC é {imc:.2f}. Você está com o peso normal')
elif SOBREPESO:
    print(f'Seu IMC é {imc:.2f}. Você está com sobrepeso')
elif OBESIDADE_GRAU1:
    print(f'Seu IMC é {imc:.2f}. Você está com obesidade grau 1, cuidado')
elif OBESIDADE_GRAU2:
    print(f'Seu IMC é {imc:.2f}. Você está com obesidade grau 2, cuidado')
else:
    print(f'Seu IMC é {imc:.2f}. Você está com obesidade mórbida, cuidado')
