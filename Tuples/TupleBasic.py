# Tuples are ordered,allows duplicates,immutable, once created cant be altered

points = (1.4, 5.2, 0.9)

print(type(points))
print(points)
print(points[1])
# TypeError: 'tuple' object does not support item assignment
#points[2] = 6.4

names = ("abc")
print(type(names))  # <class 'str'>

names_tup = ("abc",)
print(type(names_tup))
