#MODULOS: archivo que contiene un conjunto de códigos o un conjunto de funciones que se pueden incluir en una aplicación

""" Un módulo podría ser un archivo que contenga una sola variable, una función o una gran base de código. """

""" ¡¡¡TENER CUIDADO, CUANDO SE GUARDA NO DEBE QUEDAR ASI!!! """
Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def generateFullName(firstName, lastName):
	return first + " " + lastName

""" MODIFICAR DENTRO DEL ARCHIVO SI ES NECESARIO """


""" ASI DEBE DE QUEDAR """
def generateFullName(firstName, lastName):  # SIN >>>
	return first + " " + lastName             # SIN LA INFORMACION DE PYTHON: 3.11.3 (TAGS)....





#Syntax
# myModule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

#IMPORTAR UN MODULO

import myModule
myModule.generateFullName("victor", "khan") #victor khan


#IMPORTAR FUNCIONES DE UN MODULO

from myModule import generateFullName, funcion2, funcion3, ...
generateFullName("victor", "khan")        #victor khan


#IMPORTAR FUNCIONES DE UN MODULO Y RENOMBRARLAS

from myModule from generateFullName as fullName
fullName("victor", "khan")





#IMPORTAR MODULOS INCORPORADOS


""" OS MODULE """

""" usando el modulo OS de python se pueden realizar varias tareas del sistema, el modulo OS provee funciones para:
    crear, cambiar los directorios mientras estan funcionando y remover directorios(carpetas), obteniendo su contenido,
     cambiando e identificando el directorio actual."""

import os                   # importa modulo OS
os.mkdir('directory_name')  # crea carpeta
os.chdir('path')            # cambia la direccion de la carpeta
os.getcwd()                 # obtiene la carpeta actual
os.rmdir()                  # elimina la carpeta


""" SYS MODULE """

""" El módulo sys proporciona funciones y variables que se utilizan para manipular diferentes partes del entorno de tiempo de ejecución de Python.
    La función sys.argv devuelve una lista de argumentos de la línea de comandos pasados ​​a un script de Python. 
    El elemento en el índice 0 de esta lista siempre es el nombre del script, en el índice 1 está el argumento pasado desde la línea de comando. """

import sys      #importa systema
sys.exit()      #para salir del sistema
sys.maxsize     #para conocer el largo de una variable entera
sys.path        #para conocer la ubicacion
sys.version     #para conocer la version de python

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # imprime: archivo argumento1 argumento2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

#sys.argv[0]  archivo python
#argv[1]      argumento 1
#argv[2]      argumento 2

""" Se debe hacer desde la línea de comandos y no desde el intérprete interactivo de Python, tambien se debe usar desde el mismo archivo script """

cd C:\...\notebooks python main.py victor khan

#ejemplo
import sys
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

#ahora usar cmd

cd C:\...\notebooks python main.py victor python    

"""SALDRA: welcome victor. Enjoy python challenge! """


""" MODULO Statistic """

""" El módulo de estadísticas proporciona funciones para estadísticas matemáticas de datos numéricos. 
    Las funciones estadísticas populares que se definen en este módulo: media, mediana, moda, desviación estándar, etc. """

from statistics import *      # importa todas los modulos de statistics
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))             # ~22.9
print(median(ages))           # 23
print(mode(ages))             # 20
print(stdev(ages))            # ~2.3

""" MODULO Math """

""" Este modulo contiene muchas operaciones y constantes matemeticas """

from math import *       # importa todos los modulos de math
print(math.pi)           # 3.141592653589793, constante de PI
print(math.sqrt(2))      # 1.4142135623730951, raiz cuadrada
print(math.pow(2, 3))    # 8.0, funcion exponencial
print(math.floor(9.81))  # 9, redondeando al menor
print(math.ceil(9.81))   # 10, redondeando al mayor
print(math.log10(100))   # 2, logaritmo con 10 de base


""" MODULO String """

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


""" MODULO Random """
from random import random, randint
print(random())             # si no tiene argumentos, retorna valores entre 0 y 0.9999
print(randint(5, 20))       # retorna un numero entero entre [5, 20]





#EJERCICIOS

#1:

import random                                           #llamando al modulo random
def randomUserID():                                     #funcion random
  character = "abcdefghijklmnopqrstuvwxyz0123456789"    #variable alfanumerica guardada
  userId = ""                                           #variable userID vacia
  for index in range(6):                                #itera index 6 veces, es decir, se repite 6 veces el codigo
    userId += random.choice(character)                  #userID = userID + eleccion random de character (se realiza 6 veces)
  return userId                                         #retorna userID con 6 numeros/letras 

randomUserID()
