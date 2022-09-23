numbers = [2, 4, 5, 6, 7, 8, 9]
even_numbers = list(range(10))

# add at end(stack)
numbers.append(10)
print(numbers)

# add at index
numbers.insert(2, 11)
print(numbers)

# append anpther list
numbers.extend(even_numbers)
print(numbers)
