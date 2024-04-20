# Ejercicio 4: Contador de Vocales.
# Crea un programa que cuente el número de vocales en una palabra ingresada por el ususario.

palabra = input("Escribe una palabra: ")
vocales = "aeiouAEIOU"

def contador_vocales(palabra):
   contador = 0
   for letra in palabra:
      if letra in vocales:
         contador += 1
   return contador
                            
total_vocales = contador_vocales(palabra)

print(f" La palabra '{palabra}' tiene {total_vocales} vocales.")                     
