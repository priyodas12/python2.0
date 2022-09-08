def check_odd(num):
    return num % 2 == 1


nums = [2, 3, 5, 7, 8, 10]
print(list(filter(check_odd, nums)))
