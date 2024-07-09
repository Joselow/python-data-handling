custom_greet = lambda greet, name = 'juan' :  f"{greet}, {name}"

print(custom_greet('Hoal wn', 'pablo'))


print((lambda x : x * 2))    # imprime una referencia de lambda
nums = [1, 2, 3, 4]

def mapper (x):
  return x ** 3

cube = list(map(mapper, nums))

squared = list(map(lambda x: x** 5, nums))
print(squared), cube 

