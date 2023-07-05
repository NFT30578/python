# syntax
if condicion:
    codigo para la condicion verdadera


a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number


# If Else

# syntax
if condition:
    codigo para la condicion verdadera
else:
    codigo para la condicion falsa
    
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# if else elif

# syntax
if condition:
    code
elif condition:
    code
else:
    code

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# forma abreviada

# syntax
code if condition else code

a = 3
print('A is positive') if a > 0 else print('A is negative') # si la primera condicion es correcta, 'A is positive' sera mostrada

# condiciones anidadas

# syntax
if condition:
    code
    if condition:
    code

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# se pueden omitir estas condiciones usando el operador and

#condicionales if y operadores logicos and

# syntax
if condition and condition:
    code

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

#condicional if y operadores o

# syntax
if condition or condition:
    code

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
