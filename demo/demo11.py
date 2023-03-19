from functools import reduce

a = reduce(lambda x, y: x + y, [1, 2])

print(a)
