# Ejercicio 10: Determinar el Día de la semana.
# Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.)

dia_semana = int(input("Inserta un número del 1 al 7: "))
if dia_semana == 1:
    print ("Hoy es lunes")
elif  dia_semana == 2:   
    print ("Hoy es martes")
elif  dia_semana == 3:   
    print ("Hoy es miércoles")
elif  dia_semana == 4:   
    print ("Hoy es jueves")
elif  dia_semana == 5:   
    print ("Hoy es viernes")
elif  dia_semana == 6:   
    print ("Hoy es sabado")
elif  dia_semana == 7:   
    print ("Hoy es domingo")
else:    
    print ("El número elegido no es correcto por favor elija un número del 1 al 7")