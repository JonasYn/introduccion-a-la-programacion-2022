#Modifique el script anterior para que mantenga el funcionamiento, pero
#ahora, cuando el número no es mayor que 10, también se muestre un
#mensaje “Tu número (N) es menor o igual que 10!”.

def mayor_a_10 (x):
    if x > 10:
       respuesta = print (f"tu numero {x} es mayor que 10!")
    else:
        respuesta = print (f"tu numero {x} es menor o igual que 10!")
    return respuesta

numero= int(input(f"ingrese un numero"))

mayor_a_10 (numero)