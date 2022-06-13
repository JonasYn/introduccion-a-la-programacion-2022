# Escribir una función que reciba una cadena de unos y ceros (es decir, un número en
# representación binaria) y devuelva el valor decimal correspondiente.

def pasar_binario_a_decimal(x):
    resultado =  0
    for i, numero in enumerate (x[::-1]):
        resultado += (2**i) * int(numero)

    print (resultado)

pasar_binario_a_decimal("1001")
