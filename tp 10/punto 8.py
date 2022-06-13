# Escribir una función que reciba una cadena que contiene un largo número
# entero y devuelva una cadena con el número y las separaciones de miles. Por
# ejemplo, si recibe '1234567890', debe devolver '1.234.567.890'.

def poner_punto_miles (x):
    numero = ""
    for i, letra in enumerate(x[::-1]):
        if i % 3 == 0 and i != 0:
            numero += "." + letra
        else:
            numero += letra
    return (numero[::-1])

print (poner_punto_miles("1234567890"))