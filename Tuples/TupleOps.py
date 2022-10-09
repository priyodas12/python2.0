example = tuple(["abc", 9.0, 120, 'b', True])

print(type(example))
print(example)

# accessing elements
print(example[3])
print(example[-1])

# iteration
for x in example:
    print(x)

# check if exist
if "a" in example:
    print("Exist!")
else:
    print("!Sorry")

# check index
print(example.index("b"))
