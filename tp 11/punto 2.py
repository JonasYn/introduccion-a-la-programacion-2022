# Dada una lista de números enteros, escribir una función para cada uno de los
# siguientes ítems:
# a- Devuelva una lista con todos los números que sean primos.
# b- Devuelva la sumatoria y el promedio de los valores.
# c- Devuelva una lista con el factorial de cada uno de esos números.

lista = [12,3,2,1,11]


def primos(numero):
    contador = 0
    for i in range (1, numero+1):
       if numero % i == 0:
        contador +=1
    return contador == 2

def es_primo(lista):
    lista_de_primos = []
    for numero in lista:
        if primos(numero):
            lista_de_primos.append(numero)
    return lista_de_primos 

def sumatoria(lista):
    suma = 0
    for numero in lista:
        suma += numero      
    promedio = suma // len(lista)
    return suma, promedio

def cuenta_factorial(numero):
    factorial = 1
    for i in range (1,numero+1):
        factorial *= i
    return factorial

def factorial(lista):
 lista_factoriaL =[]
 for i in lista:
     lista_factoriaL.append(cuenta_factorial(i))
 return lista_factoriaL

print (f"los primos de la lista son{(es_primo(lista))}")
print (f"la sumatoria y el promedio son{(sumatoria(lista))}")
print (f"los factoriales de la lista son{(factorial(lista))}")