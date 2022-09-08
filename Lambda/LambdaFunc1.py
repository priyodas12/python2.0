def skw(num):
    return num**2


nums = [2, 5, 7, 9]

print(map(skw, nums))

for item in map(skw, nums):
    print(item)

print(list(map(skw, nums)))
