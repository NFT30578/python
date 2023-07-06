# WHILE 

# syntax
while condition:
    code goes here

count = 0
while count < 5:
    print(count)
    count = count + 1 # muestra un contador hasta 4, porque no tiene el simbolo "=" 

# tambien puede tener un else

count = 0
while count < 5:
  print (count)
  count = count + 1
else:
  print ("nada")

# Break y continue

# Break se usa cuando se quiere salir o parar el loop, sirve tambien para parar el bucle antes de que se complete

while condition:
    code goes here
    if another_condition:
        break

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# Continue puede saltar la iteracion y continua con el siguiente, tambien sirve para saltar un paso dentro del bucle

  # syntax
while condition:
    code goes here
    if another_condition:
        continue


count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1





# FOR

# For es usado para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena).

# syntax para numeros
for iterator in lst:
    code goes here

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number es un nombre temporal para referirse a los items de la lista, valido solo dentro de este loop
    print(number)       # los numeros seran mostrados linea por linea, de 0 a 5
  

# syntax para cadenas de texto

for iterator in string:
    code goes here

language = 'Python'
for letter in language:
    print(letter)     # se mostraran las letras linea por linea


for i in range(len(language)):  # genera una secuencia de números desde 0 hasta la longitud de la lista language menos uno, es decir, [0, 1, 2, 3, 4,5]
    print(language[i])          # el bucle for recorre esta secuencia de números y, para cada número i, accede al elemento en la posición i de la lista language usando el índice language[i]
                                # imprimiendo todas las letras de language(python) linea por linea
                                # en esta ocasion se usa para recorrer una secuencia de números generada por la función range, pero tambien se puede usar normalmente para texto

# syntax para tuples

# syntax
for iterator in tpl:
    code goes here

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
  
# syntax para diccionarios

  # syntax
for iterator in dct:
    code goes here


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)        # imprime las llaves solamente como: "first_name"

for key, value in person.items():
    print(key, value) # imprime las llaves y los valores

# syntax en set

for iterator in st:
    code goes here

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# syntax en rangos

# los primeros 2 argumentos definen el inicio y el final de la secuencia, el incremento viene por defecto en 1
for iterator in range(start, end, step):

lst = list(range(11))   # el ultimo parametro no lo toma, hay sumarle 1 para que tome el 11
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))  # se necesita al menos un 1 argumento (final), para crear la secuencia de rango
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

for number in range (11):
  print (number)      # se imprime del 0 al 10, sin incluir el 11



# BUCLES ANIDADOS

# syntax
for x in y:
    for t in x:
        print(t)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:                       # para todas las llaves en persona, hacer:
    if key == 'skills':                  # si la llave es igual a "skills" se ejecuta el codigo de abajo
        for skill in person['skills']:   # almacena todas las skills en la variable skill
            print(skill)                 # imprime todas las skills



# FOR ELSE

# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)


# PASS

# en python cuando una declaracion es requerida (despues del semicolon(:)) pero no se quiere ejecutar ningun codigo ahi
# se escribe la palabra pass para evitar errores o se puede usar como marcador para futuras declaraciones

for number in range(6):
    pass




#ejercicios

#1:
count = [0,1,2,3,4,5,6,7,8,9,10]
for number in count:
    print(number)

numero = 0
while numero >=0:
    print(numero)
    numero = numero +1

#2:
count.reverse()
for number in count:
    print (number)

while numero <=10:
    print(numero)
    numero = numero -1


#3:
count=1
p="a"
 while count <= 7:
	print(p)
	count = count +1
	p = p+"a"

#4:
for fila in range(8):
    for columna in range(8):
        print("# ", end="") # end="" evita que se agrege un salto de linea despues de cada caracter impreso
    print()

#5:
number = 0
for fila in range (11):
	print (number,"x",number,"=",number*number)
	number = number + 1

#6:
lista = ["Python","Numpy","Pandas","Django","Flask"]
for l in lista:
  print (l)

#7:
for even in range(0,101,2):
  print(even)

for even in range(0,101):   #mismo resultado, diferente codigo 
  if even % 2 == 0:
    print(even)

#8:
for even in range(0,100):
  if even % 2 != 0:
    print (even)

#ejercicios 2

#1:
suma = 0
>>> for i in range(0,101):
	suma += i
	if suma == 5050:
		print("The sum of all numbers is:", suma)

#2:
sumaPar = 0
sumaImpar = 0
for i in range(0,101):
  if i % 2 == 0:
    sumaPar += i
  else:
    sumaImpar += i
    break
  print ("The sum of all evens is:", sumaPar)
  print ("The sum of all odds is:", sumaImpar)  
