# Ejercicio 14: Calculadora de Descuento.
# Crea un programa que calcule el precio final de un articulo después de aplicar un descuento del 20%.

precio = float(input("Introduce el precio de un producto en euros:"))

descuento = 20 / 100
descuento_realizado = precio * descuento
precio_final = precio  - descuento_realizado

print(f"El precio final con un descuento del 20% es {precio_final:.2f} euros.")