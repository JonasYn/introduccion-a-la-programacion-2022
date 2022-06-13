# Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
# programa debe ser capaz de solicitarle al usuario que reingrese el número
# cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
# vez que detecte un error de validación, informele al usuario cuál fue el error, con
# los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
# fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
# válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.


numeros = 0


while numeros != "listo":
    numeros = (input (f"ingrese un numero del 1 al 100"))
   
    if  not numeros.isdigit():
        print (f" el dato ingresado no es numerico ")
        


    elif int (numeros) >= 0 and int (numeros) <= 100:
         print (f"{numeros} es valido. Gracias ") 
         numeros = "listo"

    elif int(numeros) <0 or int(numeros) > 100:
        print (f"El número ingresado está fuera del rango permitido. Ingrese un numero valido")
      
    
    #elif numeros == str:
        
   
        
    # else: 
    #     print (f"El dato ingresado no es numérico.")
    #     numeros = int(input (f"ingrese un numero del 1 al 100"))
    
    
    