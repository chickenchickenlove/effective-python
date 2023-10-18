def func(a, b):
    try:
        return (True, a/b)
    except ZeroDivisionError:
        return (False, None)


success, value = func(5, 0)
if success:
    print('do your action.')
