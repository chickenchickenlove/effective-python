def func(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None


result = func(5, 0)
if result is None:
    print('result is None')
else:
    print('do your action.')


if not func(5,0):
    print('false')

if not func(0,5):
    print('false')