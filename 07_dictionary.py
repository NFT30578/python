# Colección de tipos de datos no ordenados, modificables (mutables) emparejados (clave: valor).

# sintax
empty_dict = {}

# diccionario con valores de datos
dct = {"key1":"value1", "key2":"value2","key3":"value3","key4":"value4","key5":"value5",}

person = {
  "firstName":"victor",
  "lastName": "khan",
  "age": 40,
  "country": "chile",
  "isMarred": True,
  "skills": ["javascript","react", "node","mongoDB", "python"],
  "address": {
    'street': "clinton",
    'zipCode': 445667
  }
}

# acceder a los valores del diccionario

print(dct["key1"])
print(person [country]) #chile
print(person [skills])  #javascript, react, node, mongoDB, python
print(person [skills][2]) #node

# añadiendo items al diccionario

dct ["key5"] = "value5"
person["jobTittle"] = "instructor"  #añade un nuevo dato al diccionario
person["skills"].append("HTML") #añade un nuevo valor a la lista skills
print(person)

#modificar items en diccionario

dct ["key1"] = "newValue"
person["age"] = 50
person["firstName"] = "luigi"

#revisando items en diccionario (booleano)

print("key" in dct)
print("age" in person)  #TRUE
print("city" in person) #FALSE

# remover items 

person.pop('firstName')        # elimina el item firstname
person.popitem()                # elimina el ultimo item
del person['isMarried']        # elimina el item isMarred

# cambiar diccionario a lista

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # items del diccionario ([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

print(person.items()) #dict_items([('firstName', 'victor'), ('lastName', 'khan'), ('age', 40), ('country', 'chile'), ('isMarred', True), ('skills', ['javascript', 'react', 'node', 'mongoDB', 'python']), ('address', {'street': 'clinton', 'zipCode': 445667})])

# limpiar diccionario

person.clear()

# eliminar diccionario

del person

# copiar diccionario

person = {}
copiaPerson = person.copy()

# obtener los nombres de los items del diccionario

person.keys()

# obtener los valores de los items del diccionario

person.values()