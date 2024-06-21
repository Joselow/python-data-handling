dict = {}

for i in range(1, 11):
  dict[f"value_{i}"] = i * 2

# print(dict)

cool_dict = { f"value_{i}": i*2 for i in range(1, 11)}
print(cool_dict)

names = ['Juan', 'Juana', 'Pablo']
ages = ['15', '25', '48']


dict_info = { name: age for (name, age) in zip(names, ages) }
print(dict_info)


# for (key, value ) in dict.items():   # devuelve una lista de tuplas, las tuplas se pueden sacar su clave y valor
#   print(key, value)

print('-------')
# for with tuples
tupless = [('juan', 54, False), ('juan', 54, True ), ('juan', 54, True)]    

for (key, value, other) in tupless:       # al rrecorrer una lista de tuplas, cada tupla puede ser extraida sus valores ojo que debens er de la misma longitud o fallará
  print(key, value, other)

# for with array
for (index, item) in enumerate(names):     # -- crea un iterable de tuplas , siendo cada tupla el (indice, elmento)
  print(index, item)