### LISTAS ###

#similar a los arreglos, la diferencia es que con las listas se pueden hacer unas operaciones mas
#es una forma de agrupar datos
miLista = list("hola")
miOtraLista = [35, 24, 23, 13, 16, 14, 22, 22]

print(len(miLista))     #cuenta el numero de caracteres
print(miOtraLista)      #cuenta el numero de elementos dentro de una lista
print(miOtraLista[1])   #imprime el elemento en especifico

print(miOtraLista.count(22))    #cuenta el numero de veces que se repite dentro de una lista

# Asignar parametros desde una lista

lista = [35, 1.78, "victor", "khan"]    #elementos de una lista
age, height, name, surName = lista      #variables capturando el valor de la lista
print(name)

miOtraLista.insert(1,99)    #inserta una nuevo elemento a la lista = insert(lugar a insertar, elemento)
print(miOtraLista)

miOtraLista.remove(99)      #elimina un elemento de una lista, al dejarlo vacio elimina el primer parametro
print(miOtraLista)

miOtraLista.pop(0)          #saca de una lista un elemento, al estar vacio se quita el ultimo
print(miOtraLista)

elemento = miOtraLista.pop(0)   #se puede mover el elemento sacado a otra lista o variable
print(elemento)

del elemento                #elimina las variables
print(elemento)

miNuevaLista = miOtraLista.copy()   #copia el contenido de la lista
print(miNuevaLista)

miOtraLista.clear()         #vacia los elementos guardados en una lista

miOtraLista.reverse()       #ordena los elementos de forma inversa
print(miOtraLista)

miOtraLista.sort()          #ordena los elementos de la lista
print(miOtraLista)
