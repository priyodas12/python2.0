from collections import Counter

string_1 = "ashajhakaaaasklkslll"

my_counter = Counter(string_1)

print(my_counter.keys())
print(my_counter.values())
# counter dictionary
print(my_counter)
# list of tuples
print(my_counter.most_common())

print(list(my_counter.elements()))
