def five_percent_sum(a, b):
    # pass any tuple or list in sum()
    # return sum((a, b)) * 0.05
    return sum([a, b]) * 0.05


print(five_percent_sum(34, 46))


def six_percent_sum(*nums):
    return sum(nums) * 0.06


print(six_percent_sum(34, 46, 56, 90, 34))
