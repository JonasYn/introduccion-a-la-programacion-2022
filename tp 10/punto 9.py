# Escribir funciones que dada una cadena de caracteres devuelva solamente las letras
# consonantes. Por ejemplo, si recibe 'algoritmos' debe devolver 'lgrtms'.

def letras_consonates(x):
    resultado = ""
    for i, letra in enumerate(x):
        if "a"  not in letra:
            if "e"  not in letra:
                if "i"  not in letra:
                    if "o"  not in letra:
                        if "u"  not in letra:
                         resultado += letra 
    return resultado

print (letras_consonates("algoritmos"))