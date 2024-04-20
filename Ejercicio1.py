# Ejercicios Introducción a Python: Enunciados.

# Ejercicio 1: Conversor de Temperatura.
# Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.

celsius = float(input("Introduce una temperatura en grados Celsius: "))

def celsius_a_fahrengeit(celsius):
    return (9/5 + celsius + 32)
farhengeit=celsius_a_fahrengeit(celsius)

print(f"Los {celsius} grados Celsius son {farhengeit} grados Fahrenheit")
