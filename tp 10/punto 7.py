# Escribir funciones que dada una cadena de caracteres:
# I. Imprima los dos primeros caracteres.
# II. Imprima los tres últimos caracteres.
# III. Imprimir dicha cadena en sentido inverso.




def cadena_de_caracteres1(x):
    print (x[0],x[1])    

def cadena_deCaracteres2(x):
    respuesta = ""
    for i in range (len(x)):
        if i <= 1:
            respuesta = respuesta + x [i]
    print (respuesta)

def cadena_negativa(x):
    print (x[-2], x[-1])

def cadena_inversa(x):
    respuesta = x[::-1]
    print (respuesta)

variable = "Hola mundo"
cadena_de_caracteres1 (variable)
cadena_negativa (variable)
cadena_inversa (variable)
