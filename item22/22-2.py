def log(message, *values):
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print(f'{message}: {value_str}')

# 가변 변수를 사용하는 경우, 빈 리스트를 제공하지 않아도 됨.
log('안녕')
log('내 숫자는', [1,2])