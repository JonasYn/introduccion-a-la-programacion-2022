#Cree un script que le solicite al usuario ingresar un número por teclado, y
#luego le informe en pantalla si su número es mayor que 10; antes de finalizar
#e independientemente de lo que haya sucedido antes, el script mostrará un
#mensaje de despedida. Ejemplos de cómo debería verse la salida del script:

def mayor_a_10 (x):
    if x > 10:
       respuesta = print (f"tu numero {x} es mayor que 10!")
    else:
        respuesta = print (f"saludos!")
    return respuesta

numero= int(input(f"ingrese un numero"))

mayor_a_10 (numero)