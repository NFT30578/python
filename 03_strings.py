### Strings ###

myString = "mi string"

#funcion len = largo del caracter

len(myString)

# Espaciado

print(myString + " " + "hola")
print(myString, "hola")

# Salto con linea

print(myString + "\n" + "hola")
print(myString,"\n","hola")

# Salto con tabulacion

print(myString + "\t" + "hola")
print(myString, "\t", "hola")


# Escapado

print(myString + "\\n" + "hola")
print(myString, "\\t", "hola")


# Formateo

""" 
{}.format() = para variables sin formatear
"%s" %()    = para variables ya formatedas
%s para formatear en str 
%d para formatear en int
"""

name, surname, age = "victor", "khan", 35 

print("hola mi nombres es {} {} y mi edad es: {}".format(name, surname, age))
print(f"hola, mi nombre es: {name} {surname} y mi edad es: {age}")
print("hola mi nombres es %s %s %d" %(name, surname, age))

# Desempaquetados de caracteres
palabra = "python"
a, b, c, d, e, f = palabra

print(a,b,c,d,e,f)

# Division

palabraPartida = palabra[1:3]
palabraPartida = palabra[-2]
palabraPartida = palabra[1:]
print(palabraPartida)

# Reverse (cambia el orden de la palabra)

reversePalabra = palabra[::1-2]
print(reversePalabra)

# Funciones

palabra = "python"
print(palabra.capitalize())        #cambia el primer string en mayuscula
print(palabra.upper())             #transforma el string en mayuscula
print(palabra.upper().isupper())   #transforma el string en mayuscula y verifica si esta en mayuscula
print(palabra.count("p"))          #cuenta las letras
print(palabra.lower())             #transforma a minuscula
print(palabra.isnumeric())         #verifica si es un numero
print(palabra.startswith("p"))     #verifica si comienza con la letra: "p"
