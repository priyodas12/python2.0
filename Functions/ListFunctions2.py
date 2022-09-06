test_List = [1, 4, 6, 8, 9, 13, 15, 16]


def find_all_even_numbers(any_list):
    return_list = []
    for num in any_list:
        if num % 2 == 0:
            return_list.append(num)
        else:
            pass
    return return_list


print(find_all_even_numbers(test_List))
