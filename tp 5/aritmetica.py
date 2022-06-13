#Cree una función que reciba dos números como parámetro, y muestre en
#antalla la suma aritmética de ambos. Invoque a la función con dos números
#leídos desde teclado.
def aritmetica (x,y):
    suma = (x + y)
    print (suma)

numero1= int(input(f"ingrese un numero"))
numero2 = int(input(f"ingrese un numero"))

aritmetica (numero1,numero2)