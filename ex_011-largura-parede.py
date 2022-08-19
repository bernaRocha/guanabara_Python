largura = float(input("Qual a largura da parede: "))
altura = float(input("qual a altura da parede: "))
area = largura * largura
print(f'Sua parede tem a dimensão de {largura} de largura por {altura} de altura, área total de {area:.2f} m2 ')

total_tinta = area / 2

print(f"Para pintar essa parede você precisará de {total_tinta:.2f} litros de tinta")