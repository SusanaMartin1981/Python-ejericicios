# Ejercicio 7: Calculadora Simple.
# Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.

def suma (a,b):
    return a + b
def resta (a,b):
    return a - b
def multiplicacion (a,b):
    return a * b
def division (a,b):
    if b !=0:
      return a / b
    else:
        return "Error: no se puede divir entre cero."
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))    
operacion = input("Elige la operación aritmetica que quiera hacer (+, -, *, /): ")
if operacion == "+":
    resultado = suma (numero1, numero2)
elif  operacion == "-":   
    resultado = resta (numero1, numero2)
elif  operacion == "*":   
    resultado = multiplicacion (numero1, numero2)
elif  operacion == "/":   
    resultado = division (numero1, numero2)

else:
    resultado = "opcion no valida. Por favo, elige una opción valida (+, -, *, /): "  
print(f"El resultado de la operación es: {resultado}")      