# Ejercicio 6: Verificación de Palíndromo
# Crea un programa que verifique si una palabra ingresada por el ususario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

palabra_partida = input("Introduce una palabra: ")
palabra_nueva =palabra_partida[::-1]

if palabra_partida == palabra_nueva:
  print(f"Esta palabra '{palabra_partida}' es un palíndromo.")

else:
   print(f"Esta palabra '{palabra_partida}' no es un palindromo.") 
