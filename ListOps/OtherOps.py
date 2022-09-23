numbers = [21, 4, 51, 6, 17, 82, 9]

# sorting of elements: ascending always
numbers.sort()
print(numbers)

# sorting  in descending
numbers.sort(reverse=True)
print(numbers)

# reverse a list
numbers.reverse()
print(numbers)

# copy of list(shallow copy)
numbers_copy = numbers.copy()
numbers_copy.append(20)
print(numbers)
print(numbers_copy)
