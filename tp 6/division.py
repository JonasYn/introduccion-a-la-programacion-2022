# Las estructuras alternativas pueden utilizarse para validar datos. Por
# ejemplo, si se intenta crear una función que tome dos enteros como
# parámetro y muestre el resultado de su división, puede ocurrir un error si el
# denominador es cero. Utilice la estructura alternativa para validar que el
# denominador no sea cero; en caso de serlo, la función deberá mostrar el
# mensaje “No se puede dividir por 0!” en lugar de intentar mostrar el
# resultado.

def division (x,y):
    if  y == 0:
        resultado = print (f"no se puede dividir por 0")
    else:
        cuenta =  x/y
        resultado = print (f"el resultado de la division es {cuenta}")
    return resultado

numero1 = int(input(f"ingrese un numero"))
numero2 = int(input(f"ingrese un denominador"))

division (numero1,numero2)