def test_func(*args, **kwargs):
    print(args)
    print(kwargs)


test_func(1, 2, 3, 4, 5, p1=10, p2=90, p3=67)
