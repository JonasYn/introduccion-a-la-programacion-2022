ingresar_temperatura = input(f"ingrese la temperatura en celsius entre -18 y 50: ")

ancla = True
contador = 1

while ancla:

    contador += 1
   
    if ingresar_temperatura.isalpha():
         ingresar_temperatura = input(f"El dato {ingresar_temperatura} no es valido, reintentelo: ")
    elif ingresar_temperatura.isnumeric():
        if int(ingresar_temperatura) > -18 and int(ingresar_temperatura)< 50:
             print (f"el dato {ingresar_temperatura} es valido. Adios")
             ancla = False
             
        else:
            ingresar_temperatura = input(f"El dato {ingresar_temperatura} no es valido, reintentelo: ")
    else:
        ingresar_temperatura = input(f"El dato {ingresar_temperatura} no es valido, reintentelo: ")
    if contador == 10:
        print ("“Usted está jugando conmigo, yo me retiro”.")
        ancla = False
    
    
