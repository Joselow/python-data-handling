
names = ["alice", "bob", "charlie"]
nums = [1, 2, 3, 4, 5]
words = ("hello", "world", "python", "map")

def to_upper (names: list)->list:
  return map(str.upper, names)  

build_doubles = lambda nums : map(lambda x: x * 2, nums)

calc_len = lambda words : map(len, words)


def run ():
  mayus = to_upper(names)
  print(list(mayus))
  
  doubles = build_doubles(nums)
  print(list(doubles))  

  lengths = calc_len(words)
  print(set(lengths))

run()