"""
- coleccion de distintos elementos desordenados y sin indexar
- se usa en python para almacenar items unicos 
- es posible encontrar la unión, intersección, diferencia, diferencia simétrica,
  subconjunto, superconjunto y conjunto disjuntos entre conjuntos.  
"""

#sintaxis

miSet = {"hola", "mundo", 1}
miSet2 = set("hola",3,4,"mundo")

#revisando items en set (boolean)

prueba = {"hola", 3}
# print("este set tiene numero "3" ", 3 in set) retorna valor booleano

print(3 in prueba)

#añadiendo items

fruta = {"manzana"}
fruta.add("naranja")
fruta

#actualizar

hombres = {33, 20, 11}
mujeres = {29, 15, 22}
hombres.update(mujeres) # añade set de mujeres de forma desorganizada
hombres

#remover

verduras = {"tomate", "papa", "zanahoria"}
verduras.remove("papa")
verduras

#vaciar sets

palabra = {33, "papa"}
palabra.clear()
palabra

#borrar sets

comida = {"arroz", "fideos", "sopa"}
del comida  #elimina la variable junto al contenio
comida

#convertir listas a set


convertList = ["hola", "mundo", "python"]
hola = set(convertList) #al convertir lista a set se eliminan los duplicados dejando los items unicos 
type(hola)
hola

convertList = list(hola)    #tambien sirve para hacerlo a la inversa
type(convertList)
convertList

#unir sets

plantas = {"arbol", "arbusto"}
animales = {"vaca", "perro"}
planeta = plantas.union(animales)   #se obtiene el mismo resultado con update()
planeta

#encontrar items identicos

st1 = {"item1", "item2", "item3"}
st2 = {"item2", "item3", "item4"}
st1.intersection(st2)   #muestra en pantalla todos los items que se repiten entre los 2 set

#verificando subset y super set

todosValores = {1,2,3,4,5}
algunosValores = {2,3,4}
todosValores.issuperset(algunosValores)   #muestra TRUE porque algunosValores contiene una parte de todosValores
todosValores.issubset(algunosValores)     #muestra FALSE porque algunosValores no tiene mas valores que todosValores

#verificando diferencias entre 2 sets 

valor1 = {1,2,3}
valor2 = {1,2,3,4,5}
valor2.difference(valor1)   #muestra las diferencias que hay SOLO DESPUES de los valores encontrados entre los 2 set (4 y 5)

#encontrando diferencias simetricas

a = {0,1,2,3,4,5}
b = {2,3,4}
a.symmetric_difference(b)   # muestra TODAS las diferencias que NO estan entre los 2 set (0, 1 y 5) de forma ordenada 


#verifica si no hay items en comun entre 2 sets

i = {1,2,3}
r = {4,5}
i.isdisjoint(r) #mostrara TRUE porque entre los 2 sets no hay repetidos
 