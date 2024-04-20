# Ejercicio 2: Calculadora de Propina.
# Crea un porgrama que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.

total= float(input ("Introduce el total de una cuenta en euros: "))

def calculadora_propina(total):
    return (total * 1.15)
total_propina = calculadora_propina(total)

print(f" Para una cuenta de {total} euros, el monto total a paga inclyendo una propina del 15% es: {total_propina:.2f} euros")