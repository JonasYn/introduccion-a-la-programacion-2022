# Realizar una función que, dada una lista, devuelva una nueva lista cuyo
# contenido sea igual a la original pero invertida:
# Ejemplo: L1=['Di', 'buen', 'día', 'a', 'papa'] devolverá ['papa', 'a', 'día', 'buen', 'Di']

l1 = ['Di', 'buen', 'día', 'a', 'papa']

def invertir_lista1(x):
    nueva_lista = x[::-1]
    return nueva_lista


# segundo metodo

# def invertir_lista(x):
#     nueva_lista = []
#     for palabra in x[::-1]:
#         nueva_lista.append(palabra)
#     print (f"nueva lista sera {nueva_lista}")

print (invertir_lista1(l1))