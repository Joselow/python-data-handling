def cal_volumen( width: float, height: float, lenght: float)->float:
  return [{ 
    'result': (width * height * lenght), 
    'data': { 'width': width, 'height': height, 'lenght': lenght }
  }, True]

result, data = cal_volumen(45,45,45)

print(result, data)


def tries (something: any = 'Hellow world'):
  return something

print(tries())

key, value = ['number', 45]          # desempaquetado, funciona con lists, sets, tuples

print(f"{key}: {value}");

[a, b], c = [[1, 2], 3]
print(f"a: {a}, b: {b}, c: {c}")  # Output: a: 1, b: 2, c: 3


dict_example = {'key1': 'value1', 'key2': 'value2'}
v1, v2 = dict_example             # desempaqueta pero solo obtinen las claves
print(f"v1: {v1}, v2: {v2}") 


counter = 0

def increment_counter():
    global counter              # -- global nos da permiso para modificar la variable gloabal 
    counter += 1  

increment_counter()
print(counter) 

increment_counter()
print(counter)  
