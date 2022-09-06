test_list = [4, 2, 9, 5, 7]

# return true is any of the member in the list is even


def check_even_list(any_list):
    for num in any_list:
        if num % 2 == 0:
            return True
        else:
            pass


print(check_even_list(test_list))
