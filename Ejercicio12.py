# Ejercicio 12: Calculadora de Área de un Rectángulo.
# Crea un programa que calucle el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.

longitud = float(input("Introduce la longitud en centimetros: "))
ancho = float(input("Introduce el ancho en centimetros: "))

area_rectangulo =longitud * ancho

print(f"El área de un rectángulo con un alongitud '{longitud}' centimetors y un acho de '{ancho}' centimetros es igual a '{area_rectangulo: .2f}'")