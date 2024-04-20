# Ejercicio 8: Cáculo del índice de Masa Corporal (IMC)
# Escribe un programa que calcule el índice de Masa Corporal (IMD) de una persona.

peso = float(input("Introduce un peso en Kilogramos: "))
altura = float(input("Introduce una altura en metros: "))
imc = peso / (altura**2)
imc_redondeado = round(imc,2)

print(f" Para un peso de '{peso}' y una '{altura}' su indice de masa corporal es: '{imc_redondeado}'")