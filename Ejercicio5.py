# Ejercicio 5: Suma de Número Pares.
# Escribre un programa que calucle la suma de todos los números pares del 1 al 100.

def suma_pares():
    suma_pares = 0
    for numero in range(1, 101):
        if numero %2==0:
            suma_pares += numero
    return suma_pares  
resultado=suma_pares()

print(f" La suma de todos los números pares del q al 100 es: {resultado}")