# Diseñe una función que reciba una lista, vacía o no, e incorpore números hasta que
# el usuario ingrese el valor “salir”. Cuando termina de ingresar los datos, la
# función debe retornar la lista al programa principal.



lista = []
def ingresa_numeros_lista():
 
 ancla2 = True
 while ancla2:
      ingresar_numeros= input("ingrese los numeros que quiera agregar a la lista o salir para terminar: ")
      if ingresar_numeros.isdecimal():
        lista.append(ingresar_numeros)
        print (f"el numero {ingresar_numeros} es valido y se agrego correctamente a la lista")
      elif ingresar_numeros.isalpha():
           temporal = ingresar_numeros.lower()
           if temporal == "salir":
            ancla2 = False
           else:
            print (f"el dato {ingresar_numeros} es invalido, por favor reintentelo")
          
      else:
           print(f"el dato {ingresar_numeros} no es valido reintentelo o escriba salir para terminar: ")

ingresa_numeros_lista()
print (lista)