from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]

result = combinations(a, 2)

print(list(result))

result = combinations_with_replacement(a, 2)

print(list(result))
