# Ejercicio 16: Contador de Números Pares e Impares.
# Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.

entrada = input ("Introduce una lista de números enteros serparados por espacios: ")

lista_numeros = [int(x) for x in entrada.split()]

suma_par = 0
suma_impar = 0

for numero in lista_numeros:
      if numero % 2 == 0:
            suma_par += 1
      else:
            suma_impar += 1
            
print(F"En la lista introducida por el usuario encontramos {suma_par}  números pares y {suma_impar} números impares")                  