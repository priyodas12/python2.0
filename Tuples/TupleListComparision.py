import sys
import timeit
my_list = [1, 0.8, 101, "hello", False]
my_tuple = (1, 0.8, 101, "hello", False)

print(sys.getsizeof(my_list), bytes)
print(sys.getsizeof(my_tuple), bytes)

print(timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=100000))
print(timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=100000))
