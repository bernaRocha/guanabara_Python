import math
import emoji

### libs do Python: https://pypi.org/

### from math import

## floor(raiz) arredonda para baixo
## ceil(raiz) arredonda para cima

# Link da aula https://youtu.be/oOUyhGNib2Q

numero = int(input("Digite um número: "))
raiz = math.sqrt(numero)
print(f"A raiz de {numero} é {raiz:.0f}")

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize("Python is fun :red_heart:"))
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
print(emoji.emojize('Python es :pulgar_hacia_arriba:', language='es'))