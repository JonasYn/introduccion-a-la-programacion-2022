# Haciendo uso de las funciones para strings que ya conoce, implemente un
# script que haga lo siguiente:
# I. Le solicite al usuario ingresar una palabra por teclado. Se debe validar que
# la palabra tenga al menos una ‘ñ’, que no sea sólo caracteres numéricos, y
# que no sean sólo espacios en blanco. En caso de no ser válida, se le debe
# pedir al usuario que la reingrese.
# II. Informe en pantalla la cantidad de letras de la palabra ingresada.
# III. Transforme la palabra a mayúsculas, reemplace todas las ‘Ñ’ por ‘N’, y
# luego muestre el resultado en pantalla.
final = "none" 
while (final !="stop"):
    palabra = input ("por favor ingrese una palabra : ")
    if "ñ" in palabra:
        if  not palabra.isnumeric ():
            if not palabra.isspace():
                print (f"la palabra ingresada tiene {len(palabra)} letras")
            old = "ñ"
            new = "n"
            s2 = palabra.replace (old, new)
            print (f"{palabra} ahora sera {s2.upper()}")
            final = "stop"
    else:
        print ("la palabra ingresada no cumple los requisitos, intentelo de nuevo") 
        palabra = input ("por favor ingrese una palabra : ")