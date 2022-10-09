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

# copy of list(shallow copy, doese not modify original list)
numbers_copy = numbers.copy()
numbers_copy.append(20)
print(numbers)
print(numbers_copy)

# generate list with identical elemnts
identaical_elements_1 = [1]*4
print(identaical_elements_1)

# concate two list
identaical_elements_2 = [2]*5

concatenated_list = identaical_elements_1+identaical_elements_2
print(concatenated_list)

# map like operation
numbers_square_init = list(range(0, 10))

numbers_square_result = [i*i*i for i in numbers_square_init]
print(numbers_square_result)
