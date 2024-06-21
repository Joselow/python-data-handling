numbers = []

for item in range(1, 11):
  if item % 2 == 0 :
    numbers.append(item*2)

cool_numbers = [(item * 2) for item in range(1, 11) if item % 2 == 0 ]  # -- muhco mas conciso

print( numbers)
print( cool_numbers)