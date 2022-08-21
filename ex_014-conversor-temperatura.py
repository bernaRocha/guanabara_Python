"""
Conversor de temperaturas
"""

temperatura_celcius = float(input("Informe a temperatura em ºC: "))

fahrenheit = ((9 * temperatura_celcius) / 5) + 32
kelvin = temperatura_celcius + 273
print(f"A tempratura de {temperatura_celcius}ºC corresponde a {fahrenheit:.2f}ºF")
print(f"A tempratura de {temperatura_celcius}ºC corresponde a {kelvin}K")

temperatura_kelvin = float(input("Informe a tempratura em Kelvin: "))

temperatura_fahrenheit = ((temperatura_kelvin * 9/5) - 459.67)
print(f"A tempratura de {temperatura_kelvin}K em Fahrenheit é {temperatura_fahrenheit}ºF")
