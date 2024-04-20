# Ejercicio 15:  Coversion del Tiempo.
# Escibe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.

minutos = float (input ("Introduzca un número de minutos: "))

horas = 0

while minutos >= 60:
    horas = horas +1
    minutos -= 60

print(f"Seían '{horas}' y '{minutos}' minutos")    


