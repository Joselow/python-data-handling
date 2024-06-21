set_countries = { 'col', 'mex', 'bol'}

print(set_countries)


print(f"lenght of set of countries: {len(set_countries)}")
print('pe' not in set_countries)
print('col' not in set_countries)


set_countries.add('newCountry')
print(set_countries)


new_countries = {'pe', 'ne', 'ja', 'dx'}

set_countries.update(new_countries)
print(set_countries)


set_countries.remove('ne')       
set_countries.discard('neo')          # -- remove the element without throw an error
print(set_countries)


set_countries.clear()
exits_or_not ='Exists'  if len(set_countries) else 'Empty'   # -- ternaria o condicionales en línea
print(set_countries, exits_or_not)

# Operations
# -- union, intersection, difference puede recibir varios argumentos

first_set_countries = set(['col', 'mx', 'bol'])
second_set_countries = set(['pe', 'bol', 'ch'])


def unionSets (first_set, second_set):    
  # union = first_set.union(second_set)
  union = first_set | second_set

  print(f"Union: {union}")
  return union

unionSets(first_set_countries, set_countries)


def intersectionSets (first_set, second_set):
  # intersection = first_set.intersection(second_set)
  intersection = first_set & second_set
  print(f"Intersection: {intersection}")
  return intersection

intersectionSets(first_set_countries, second_set_countries)


def diferenceSets (first_set, second_set):
  # difference = first_set.difference(second_set)
  difference = first_set - second_set
  print(f"Difference: {difference}")
  return difference

diferenceSets(first_set_countries, second_set_countries)


def simetricDiffSets (first_set, second_set):     # -- solo toma un argumento
  # simetric = first_set.symmetric_difference(second_set)
  simetric = first_set ^ second_set
  print(f"Simetric: {simetric}")

simetricDiffSets(first_set_countries, second_set_countries)


def simetricDiffSetsCustom (first_set, second_set):
  first_difference =  diferenceSets(first_set, second_set)
  second_difference = diferenceSets(second_set, first_set)

  simetric = unionSets(first_difference, second_difference)
  print(f"Simetric: {simetric}")


simetricDiffSetsCustom(first_set_countries, second_set_countries)