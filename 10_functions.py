# Funcion: bloque de codigo reutilizable diseñada a realizar cierta tarea

# Syntax
def funcionName():  # declarando una funcion
  codigo

funcionName()        #llamando la funcion


def generarNombreCompleto():  # una funcion puede ser declarada sin parametros
  primerNombre = "victor"
  segundoNombre = "khan"
  espacio = " "
  nombreCompleto = primerNombre + espacio + segundoNombre
  print (nombreCompleto)
  
generarNombreCompleto()      # victor khan


def añade2numeros():
  numero1 = 2
  numero2 = 3
  total = numero1 + numero2
  print (total)

añade2numeros()


# FUNCION RETORNANDO VALOR: PARTE 1

def generarNombreCompleto():
  primerNombre = "victor"
  segundoNombre = "khan"
  espacio = " "
  nombreCompleto = primerNombre + segundoNombre
  return nombreCompleto   #si una funcion no tiene una declaracion de retorno el valor de la funcion es NONE

print (generarNombreCompleto())
generarNombreCompleto()           # igual de valido

# FUNCION CON 1 PARAMETRO: en una funcion se puede pasar varios valores como parametros como: numeros, cadenas, booleanos, listas, tuples, diccionarios o sets

# Syntax
def funcionName(parameter):   #
  code

print (funcionName(argument))
funcionName(argument)

def saludos(nombre):    # si la funcion toma 1 parametro hay que llamarlo con el argumento 
  mensaje = nombre + ", bienvenido a Python."
  return mensaje

print (saludos("victor"))  # funcion llamando al argumento
saludos("victor")


def añadir10(numero):
  diez = 10
  total = numero + diez
  return total      # return no me deja usarlo como variable para sumar:  return numero + diez

añadir10(90)


def numeroCuadrado (x):
  cuadrado = x * x
  return cuadrado

numeroCuadrado(5)

def areaDeCirculo(radio):
  PI = 3.14
  area = PI * radio ** 2
  return area

areaDeCirculo(10)

def sumaDeNumeros(numero):
  total = 0
  for indice in range (numero + 1):   # se le añade el +1 para que cuente el numero completo 
    total += indice     # al indice se le empieza a sumar el valor de la iteracion: 0+1+2+3...
  return total

sumaDeNumeros(10) # como resultado de la iteracion el valor es 55
sumaDeNumeros(100) # 5050


# FUNCION CON 2 PARAMETROS: una funcion puede tener o no varios parametros o mas 

# Syntax
def funcion(parametro1, parametro2):  # si un parametro no se va a llamar, este debe de tener algun valor, o sino Python va a lanzar ERROR
  codigo
  
print (argumento1, argumento2)        # no necesariamente se debe llamar a los 2 argumentos, pero hay que asegurarse de que el otro tenga un valor

def generarNombreCompleto(nombre, apellido):
  espacio = " "
  nombreCompleto = nombre + espacio + apellido
  return nombreCompleto

print ("nombre completo:", generarNombreCompleto("victor", "khan"))


def prueba(a, b):
  return a + b

prueba(1)       # arroja ERROR porque b no tiene un valor

def prueba(a, b=0):
  return a + b

print(1)        # no muestra ERROR porque b tiene valor 0

def suma2Numeros (numero1, numero2):
  suma = numero1 + numero2
  return suma

print ("la suma de 2 numeros es:", suma2Numeros(2,4))


def pesoDeObjeto(masa, gravedad):
  peso = str(masa * gravedad)+ " N"     # se debe transformar el resultado a texto para que se pueda sumar la N, pero se puede poner la N en el print tambien
  return peso

print ("el peso del objeto en newtons es:", pesoDeObjeto(100,9.81))


# PASANDO ARGUMENTOS CON KEY Y VALORES

#syntax
def funcion(parametro1, parametro2):
  codigo

print (funcion(argumento1 = John, argumento2 = Doe))    # el orden de los argumentos no importa aqui



def nombreCompleto(nombre, apellido):
  espacio = " "
  return nombre + espacio + apellido

nombreCompleto(nombre = "victor", apellido = "khan")


def suma(numero1, numero2):
  total = numero1 + numero2
  return total

suma(numero2 = 2, numero1 = 1)    # el orden de los numeros no importa aqui


# FUNCION RETORNANDO UN VALOR: PARTE2       # como no colocar el return arroja NONE, se tiene que colocar return seguido de la variable a retornar, se puede usar cualquier dato

#syntax

def funcion(parametro):
  return parametro

funcion(parametro)

#texto
def primerNombre(nombre):
  return nombre

primerNombre("victor")  #victor

#numero
def suma(numero1, numero2):
  total = numero1 + numero2
  return total

suma(1,2)

#booleano

def esPar(numero):
  if numero % 2 == 0:
    print ("par")
    return True     #el return termina la condicion/bucle/funcion premeturamente y almacena la variable, similar al break
  return False

print (esPar(10))   # true
print (esPar(7))    # false

#Lista
def encontrarNumerosPares(numero):
  pares = []                          #lista vacia
  for indice in range(numero + 1):    #itera en un rango de 0 a "numero" (incluyendolo)
    if indice % 2 == 0:               #si el numero es par
      pares.append(indice)            #se almacena en la variable pares con el metodo .append()
  return pares

print (encontrarNumerosPares(10))


#FUNCIONES CON PARAMETROS POR DEFECTO

#Syntax

def funcion(parametro = valor):
  codigo

print(funcion())
print(funcion(argumento))

#texto
def saludos(nombre = "victor"):                 #declara el valor victor a nombre
  mensaje = nombre + ", bienvenido a python"    #se guarda el nombre + cadena de texto
  return mensaje                                #retorna mensaje

saludos()                                       #'victor, bienvenido a python'    #victor estaba como valor predeterminado
saludos("jose")                                 #'jose, bienvenido a python'

def saludos(nombre = "victor", apellido = "khan"):  #se puede hacer con multiples parametros
  return nombre + " " + apellido

saludos()

#numero
def suma(numero1, numero2 = 1):     #se puede colocar tambien un parametro con valor,
  return numero1 + numero2          #al momento de llamar a la funcion se debe escribir el valor del parametro faltante

suma(1)                             #2        por que numero2 ya tenia como valor 1


#NUMERO DE ARGUMENTOS ARBITRARIOS: si no sabemos el numero de argumentos que se van a pasar a una funcion, se puede añadir * antes del parametro

#Syntax
def funcion(*parametro):   #al colocar *, indica que la funcion acepta un numero variable de argumentos posicionales
  codigo

funcion(parametro1, parametro2,parametro3,...)

def sumar(*numeros):         #funcion suma con numero indefinido de numeros
  resultado = sum(numeros)   #los numeros se suma con el metodo: sum() y se guardan en resultado (como son indefinidos se puede sumar infinitamente)
  return resultado

sumar( suma(2,3,5) )         #10     se puede sumar todos los numeros que se quieran 

def sumarTodosLosNumeros(*numeros): #los parametros con * se almacenan como tuplas/tuple
  total = 0                         #los parametros variables no necesariamente se usan con bucles for
  for numero in numeros:
    total += numero                 # total = total + numero
  return total

sumarTodosLosNumeros(2,3,10)



#FUNCIONES DE NUMEROS POR DEFECTO Y ARBITRARIOS

def generarGrupos(equipos, *parametro):
  print(equipos)             # Imprime el valor del argumento 'equipos'
    for indice in parametro: # Itera sobre los argumentos adicionales
      print(indice)          # Imprime cada argumento adicional en una línea separada
  
generarGrupos("equipo 1", "victor","carlos","paul")


#FUNCION COMO PARAMETRO DE OTRA FUNCION

def numeroCuadrado(numero):
  return numero * numero    #devuelve el numero al cuadrado

def hacerAlgo(f, x):
  return f(x)               #devuelve el resultado de llamar a la función f con el argumento x

hacerAlgo(numeroCuadrado, 3)  #9

#como se llama la funcion hacerAlgo, queda asi:
# f(x) = numeroCuadrado(3)
# por lo tanto numeroCuadrado obtiene el parametro 3, devolviendolo al cuadrado, es decir, 9


#ejercicios:

#1:
def add_two_numbers(param1,param2):
  sum = param1 + param2
  return sum

add_two_numbers(2,4)

#2:
def areaDeCirculo(r):
  PI = 3.14
  area = PI * r * r
  return area

areaDeCirculo(3)

#3:
def add_all_nums(*param):
  total = 0                                     #variable que va a usarse para sumar
  for number in param:
    if not isinstance(number, (int,float)):     #isinstance es una funcion que verifica si el parametro que se ponga pertenece a un tipo de dato
      print(f"Error {number} is not a number")  # arroja error de que number no es un tipo de dato numero
      return
    total += number                             #total = total + number    devuelve la suma de los numeros que se ingresaran a la funcion
  return total

add_all_nums(3,4,5)                             #12
add_all_nums(1,"cuatro",5)                      #Error cuatro is not a number

#4:
def convert_celsius_to_fahrenheit(param):
  F = (param * 9 / 5) + 32
  return F

convert_celsius_to_fahrenheit(10)

#5:
def check_season(month):
  if month in ("enero", "febrero", "marzo"):
    return "verano"
  elif month in ("abril","mayo","junio"):
    return "otoño"
  elif month in ("julio","agosto","septiembre"):
    return "invierno"
  elif month in ("octubre", "noviembre","diciembre"):
    return "primavera"

check_season("enero")

#6:
def calculate_slope(x1,y1,x2,y2):
  slope = (y2- y1) / (x2 - x1)
  return slope

calculate_slope(2,3,5,6)

#7:
