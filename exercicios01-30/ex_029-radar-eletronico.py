from time import sleep

velocidade = float(input('Qual a velocidade atual do carro? (Responda apenas com números) '))

if velocidade > 80:
    print('MULTADO! Excedeu o limite de segurança que é de 80Km/h')
    print('Calculando sua multa......')
    multa = (velocidade - 80) * 7

    sleep(2)
    
    print(f'Você deverá parar uma multa de {multa:.2f} reais')
print('Tenha um bom dia!')
