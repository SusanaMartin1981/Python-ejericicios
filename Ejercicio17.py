# Ejercicio 17: Conversosr de Millas a Kilometros.
# Escribe un programa que coniverta una distancia en millas a Kilómetors. Sabiendo que 1 milla equivale a 1.60934 Kilómetros.

milla = float(input("Escribe el número de millas: "))

def calculo_kilometros():
    kilometros = milla * 1.60934
    return kilometros

print(f"La distancia metida por el usuario en millas corresponde a {calculo_kilometros():.2f} Kilómetros")  