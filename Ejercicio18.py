# Ejercicio 18: Contador de Palabras.
# Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

oracion = input("Introduzca una oración: ")

contador = 1 
for palabra in oracion:
    if palabra == " ":
        contador +=1

print(f"La oración introducida por el usuario tiene '{contador}' palabras")        