def key_args_func(**kwargs):
    print(kwargs)
    if 'name' in kwargs:
        print('my name is {}'.format(kwargs['name']))
    else:
        print('Not Found!')


key_args_func(name='priyo', name1='priya')
