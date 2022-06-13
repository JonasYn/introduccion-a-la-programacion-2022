# Python ofrece algunas funciones built-in para facilitar la implementación de
# validaciones. A continuación se listan algunas de las más comunes:
# valor.isdigit()
# Retorna True si todos los caracteres de valor son numéricos, False en caso
# contrario.
# valor.isalpha()
# Retorna True si todos los caracteres de valor son alfabéticos (no
# numéricos), False en caso contrario.
# valor.isalnum()
# Retorna True si valor es una combinación alfanumérica (caracteres y
# números), False en caso contrario.
# Codifique una función que reciba un parámetro cualquiera proveniente del
# usuario del programa (que puede contener letras, números, o una combinación
# de ambas), e indique si el mismo es un número, una palabra, o un valor
# alfanumérico. Compruebe que su función resuelve el problema enviándole
# valores correspondientes a las tres posibilidades.

def parametrox(valor):
    if valor.isdigit():
        parametro = print(f"todos los caracteres son numericos")
    elif valor.isalpha():
        parametro = print (f"todos los caracteres son alfabeticos")
    elif valor.isalnum:
        parametro = print (f"los caracteres son mixtos entre numeros y letras")
    return parametro

valor1 = (input(f"ingrese un caracter numerico o alfanumerico o mixto"))

parametrox(valor1)
