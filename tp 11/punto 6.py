# Escribir una función que reciba una cadena a buscar y una lista de nombres
# de personas y busque dentro de la lista, todas los elementos que contengan esa
# cadena o cualquier parte de ella. Debe devolver una lista con los elementos
# encontrados.

lista_de_nombres =["messi", "mes", "mesa", "brazil", "segundo"]
cadena_a_buscar = ["mes"]

def elementos_a_buscar(cadena, lista):
    encontrados = []
    for i in lista:
        if i in cadena:
            encontrados.append(i)
    return encontrados


print (elementos_a_buscar (cadena_a_buscar, lista_de_nombres))