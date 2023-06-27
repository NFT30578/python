#variables

variable = "Mi String Variable"
# print(variable)

miNumero = 5
# print(miNumero)

miBoolean = False

#str, int, bool funciona como Parse
#concatenecíon de varibles string
print(variable, ",", str(miNumero), "," , miBoolean)

#funciones del sistema.
# len() =largo de caracteres
print(len("hola mundo"))

#variables en una sola linea
#se pueden mezclar varios tipos en una sola linea
nombre, apellido, alias, edad = "victor", "khan", "bomba", 30

print("mi nombre es:", nombre, apellido,"y mi alias es:", alias,"y edad es:", edad)




#las variables pueden sobreescribirse y cambiar el tipo de variable
#input = caja para almacenar variables
nombre = input("cual es tu nombre?")
edad = input("cual es tu edad?")

""" 
IMPORTANTE /// CUIDADO: EJECUTAR LINEA POR LINEA PARA QUE PYTHON PUEDA RECONOCER LOS PARAMETROS, OJO /// CUIDADO
"""
direccion: str = "chile"
direccion: int = 3
print(direccion)