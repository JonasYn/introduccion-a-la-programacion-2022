#A) 
# Len(variable) nos devuelve la longitud de un objeto, ya sea una lista, una cadena, una tupla o un diccionario
#ejemplo 

# aux = "Jonas"
# aux2 = 27, 25, 24

# print (len(aux) , len(aux2)) 



#B)
#  string.Lower se utiliza para pasar una cadena de caracteres a minuscula
#Ejemplo

# Mayusculas = "HOLA MUNDO"
# print (Mayusculas.lower())



#C) 
# string.Upper se utiliza para pasar una cadena de caracteres a mayusculas
#Ejemplo

# minusculas = "hola mundo"
# print (minusculas.upper())



#D)
# string.capitalize() sirve para convertir la primera letra de una cadena de caracteres a mayusculas
#ejemplo

# primer_letra = "hola mundo"
# print (primer_letra.capitalize())



#E)
# string.replace(s1,s2) sirve para remplazar un caracter en un string

# s1 = "hola planeta"
# old = "planeta"
# new = "mundo"

# s2 = s1.replace (old, new)
# print (s2)



#F)
# string.count(s1) sirve para contar la cantidad de veces que se repite un substring dentro de un string

# var = "hola hola hola hola hola hola mundo mundo mundo"
# print (var.count("hola"), var.count("mundo"))

#G)
# El método isnumeric() devuelve True si todos los caracteres de una cadena son caracteres numéricos.
#  Si no, devuelve Falso

# aux1 = "hola mundo"   #false
# aux2 = "128"          #true

# print (aux1.isnumeric(), aux2.isnumeric())



#H)
# string.ispace() devuelve true si todos los caracteres de una cadena son caracteres en blaco,
# de lo contrario dara false

# var1 = "    "   #true
# var2 = "hola mundo"   #false

# print (var1.isspace(), var2.isspace())



#I)
#  string.endswith(s1) El método Endswith() devuelve True si la cadena termina con el valor especificado;
#  de lo contrario, False .

# palabra = "code geass es god"
                        
# print (palabra.endswith("god"), palabra.endswith("bad"))
                          #true                    #false