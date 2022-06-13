#Cree un script que le solicite al usuario ingresar dos números por teclado, y
#luego indique por pantalla cuál de ellos es el mayor. Contemple la posibilidad
#de que los números sean iguales, y muestre un mensaje acorde.



def numer_mayor (x,y):
    if x > y:
        mayor = print (f"{x} es el mayor")
    elif y > x:
        mayor = print (f"{y} es el mayor")
    elif y == x:
        mayor = print(f"ambos son iguales")
    return mayor

numero1= int(input(f"ingrese un numero"))
numero2= int(input(f"ingrese un numero"))

numer_mayor (numero1,numero2)