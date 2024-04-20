# Ejercicio 9: Conversor de Divisas.
# Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.

cantidad_dolares= float(input("Introduzca la cantidad de dolares que quiere convertir a euroes: "))

tipo_de_cambio = 0.85
cantidad_euros= cantidad_dolares * tipo_de_cambio

input(f"'{cantidad_dolares:.2f}' dolares son '{cantidad_euros:.2f}' euros." )