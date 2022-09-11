list3 = [2, 5, 6, 7, 8, 9]


def skw(num):
    return num**2


print(list(map(skw, list3)))

for num in map(lambda num1: num1**2, list3):
    print(num)
