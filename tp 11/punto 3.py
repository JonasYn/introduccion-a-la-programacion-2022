# Dada una lista de números enteros y un entero k, escribir una función para
# cada uno de los siguientes ítems:
# a- Devuelva tres listas, una con los menores, otra con los mayores y otra con los
# iguales a k.
# b- Devuelva una lista con aquellos que son múltiplos de k.

lista = [19,10,2,5,6,8,7,12,18]
k = 6

def igual_menor_mayor (lista):
 lista_mayor_que_k = []
 lista_menor_que_k = []
 lista_igual_que_k = []
 for numero in lista:
    if numero > k:
        lista_mayor_que_k.append(numero)
    elif numero < k:
        lista_menor_que_k.append(numero)
    elif numero == k:
        lista_igual_que_k.append(numero)
 print (f"los menores que k son {(lista_menor_que_k)}") 
 print (f"los numeros mayores que k son {lista_mayor_que_k}")
 print (f"los numeros iguales que k son {lista_igual_que_k}")

def multiplos_de_k(lista):
 lista_multiplos_de_k= []
 for numero in lista:
        if numero % k == 0:
            lista_multiplos_de_k.append(numero)
 print (f"los multiplos de k en la lista son {lista_multiplos_de_k}")

igual_menor_mayor(lista)
multiplos_de_k(lista)