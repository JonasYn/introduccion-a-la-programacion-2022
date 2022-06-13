# Escribir una función que reciba una cadena a buscar y una lista de nombres
# de personas y busque dentro de la lista, todas los elementos que contengan esa
# cadena o cualquier parte de ella. Debe devolver una lista con los elementos
# encontrados.

lista_de_nombres =["Juan", "Pedro", "martin", "Lucas", "Jonas", "pepe", "adri", "fer","messi", "maradona"]
cadena_a_buscar = [0,2,4,6,7,8,9]

def elementos_a_buscar (x,y):
    nueva_lista = []
    for i, nombre in enumerate(x):
     for a in y:
        if i == a:
            nueva_lista.append(nombre)
    print (nueva_lista)

elementos_a_buscar (lista_de_nombres, cadena_a_buscar)