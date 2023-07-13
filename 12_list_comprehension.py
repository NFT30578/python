# Comprension de listas: es una forma corta de crear una lista

# Syntax
[i for i in iterable if expresion]

# 1ra forma
language = "Python"
lista = list(language)  # Cambiando de string a lista
type(lista) # Lista
lista # ["P","y","t","h","o","n"]

# 2da forma

lista = [i for i in language] #  [expresion for elemento in iterable if condicion]
type(lista) # Lista
lista # ["P","y","t","h","o","n"]

""" 
- expresion: es la operación que se realiza en cada elemento del iterable. Por ejemplo, elevar al cuadrado cada elemento de una lista de números, la expresión sería elemento ** 2.
- for elemento in iterable: indica que estás recorriendo un iterable, como una lista, tupla o cadena, y accediendo a cada elemento individualmente.
- if condicion: es opcional y permite filtrar elementos al crear la nueva lista. Solo los elementos que cumplan con la condición serán incluidos en la nueva lista.
"""

# 3ra forma
numbers = [i for i in range(11)]  # Genera una lista de numeros del 0 al 10
square = [i * i for i in range(11)]
tupla = [(i, i * i) for i in range(11)]

numbers # [0,1,2,3,4,5,6,7,8,9,10]

""" 
- Es posible hacer operaciones matematicas durante la iteracion
- Tambien es posible hacer una lista de tuplas
"""

# Comprension de lista con condicional if

numerosPares = [i for i in range(21) if i % 2 == 0 ] # si i % 2 = 0, crea una lista de 20 numeros pares
numerosPares

numerosImpares = [i for i in range(21) if i % 2 != 0] # si i % 2 NO es 0, crear lista de 20 numeros impares
numerosImpares

numbers = [-8,-7,-3,-1,0,1,3,4,5,7,6,8,10]
numerosParesPositivos = [numbers for numbers in range(21) if numbers % 2 == 0 and numbers > 0]
numerosParesPositivos # [2,4,6,8,10,12,14,16,18,20]

listaDeLista = [ [1,2,3], [4,5,6], [7,8,9] ]  # Lista con 3 arreglos
listaCortada = [ numero for fila in listaDeLista for numero in fila  ]  # como numero y fila no tienen valores, se van fusionando los 3 arreglos en una lista
listaCortada  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# FUNCION LAMBDA: es una pequeña funcion anonima sin nombre, puede tener cualquier numero de argumentos, pero solo 1 expresion

# muy similar a una funcion anonima de Javascript

# Syntax
x = lambda param1, param2, param3: param1 + param2 + param2
x(arg1, arg2, arg3)

def dosNumeros (a, b):
  return a + b

dosNumeros(2, 3)  # 5

# Ejemplo
añadir2Numeros = lambda a, b: a + b
añadir2Numeros(2, 3)  # 5

print( (lambda a, b: a + b) (2, 3) )  # se puede autoinvocar, pero para este metodo se necesita usar print

cuadrado = lambda x: x ** 2 # x al cuadrado
cuadrado(3)

# FUNCION LAMBDA DENTRO DE OTRA FUNCION

def power(x):
  return lambda n: x ** n

cubo = power(2)(3) # Funcion power ahora necesita 2 argumentos para ser usada, en 2 parentesis separadas
cubo  # 8


# EJERCICIOS

#1:

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numerosNegativos = [num for num in numbers if  num <= 0]
numerosNegativos

#2:

def aplanar(lista):
  resultado = []  # crea una lista vacia que almacenara los resultados
  for item in lista:  # recorre cada elemento de una lista
    if isinstance(item, list):  # verfica si el elemento es una lista
    resultado.extend(aplanar(item))  # si es una lista, llama a la funcion aplanar con el elemento como argumento y lo agrega a resultado con .extend
  else:
    resultado.append(item)  # si no es una lista, agrega el elemento directamente con .append
  return resultado  # devuelve lista aplanada

list_of_lists = [ [ [1, 2, 3] ], [ 4, 5, 6] , [ [7, 8, 9] ] ]
listaAplanada = aplanar(list_of_lists)
listaAplanada # [1,2,3,4,5,6,7,8,9]