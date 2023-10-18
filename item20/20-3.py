def func(a, b) -> float:
    try:
        return a/b
    except ZeroDivisionError:
        raise ValueError('잘못된 입력. 0으로 나눌 수 없음.')


try:
    value = func(5, 0)
except ValueError as e:
    print(f'잘못된 입력: {e}')
else:
    print('do your action.')
