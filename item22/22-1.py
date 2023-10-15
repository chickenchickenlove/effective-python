def log(message, values):
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print(f'{message}: {value_str}')

# 가변 변수를 사용하지 않는 경우, 사용하지 않더라도 리스트를 넣어야 한다.
log('안녕', [])
log('내 숫자는', [1,2])




