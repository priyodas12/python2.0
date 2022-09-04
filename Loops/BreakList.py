n_list = [2, 3, 4, 5, 6, 0, 6, 9, 7]
for num in n_list:
    # print(num)
    pass
print('end of script 1!')

for num in n_list:
    print(num)
    if (num == 0):
        print('continue')
        continue
print('end of script 2!')

for num in n_list:
    print(num)
    if (num == 0):
        print('break!')
        break
print('end of script 2!')
