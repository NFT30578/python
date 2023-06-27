###operadores aritmeticos ###

print(3+1)  # operador: suma
print(3-1)  # operador: resta
print(3*1)  # operador: multiplicacion
print(3/1)  # operador: division
print(10%2) # operador: porcentaje
print(4//3) # operador: residuo
print(3**1) # operador: potencia 

#al agregar el operador + se juntan los string
print ("hola"+str(5))

#al agregar el operador * multiplica la variable
print("hola"*5)
print("hola" * (2*3))


myFloat=2.5*2
print("hola" * int(myFloat))

### operadores comparativos ###

print(3<1)  # operador: menor que (booleano)
print(3>1)  # operador: mayor que (booleano)
print(3>=1) # operador: mayor o igual que (booleano)
print(3<=1) # operador: menor o igual que (booleano)
print(3|1)  # operador: y
print(3==1) # operador: es igual
print(3!=1) # operador: NO es igual a

#sirve tambien para las longitudes de caracteres, ambas formas estan correctas
#cuando son string compara alfabeticamente las letras de ambas tanto minusculas como mayusculas
#como por ASCII
print(len("mundo") < len("hola"))
print("aaa" < "aba")

### operadores logicos ###

#la logica booleana se muestra como:
""" 
true and true = true
true and false = false
false and true = false
false and false = false
"""
#es al reves cuando se usa el not
print(3 > 4 and "hola" > "python")
print(3 < 4 or "hola" < "python")
print( not(3 > 4))
