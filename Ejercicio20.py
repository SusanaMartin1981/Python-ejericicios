# Ejercicio 20: Suma de Números en una Lista.
# Crea un programa que sume todos los números en una lista ingresada por el usuario.

entrada = input("Introduzca lista de números enteros separados por un espacio: ")

lista_numeros = [int (x) for x in entrada.split()]
suma = 0
for numero in lista_numeros:
    suma += numero

print(f"Los números de la lista introducida suman {suma}.")    