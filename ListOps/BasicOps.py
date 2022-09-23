friends = ["alex", "bob", "julia", "max", "roy"]

# access all elements
print(friends)
# access single elements
print(friends[1])
# access elemnts from back,last elemnts starts from [-1]
print(friends[-2])

# selection of elemnts from specific index
print(friends[1:])  # from index[1] to rest
# from index[1] to index[3] where index[3] will be exclusive,list[inclusive:exclusive]
print(friends[1:3])
# reverse list
print(friends[::-1])
