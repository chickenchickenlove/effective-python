def log(seq, message, values):
    if not values:
        print(f'{seq} - {message}')
    else:
        value_str = ', '.join(str(x) for x in values)
        print(f'{seq} - {message}: {value_str}')

# 이 경우, TypeError: log() missing 1 required positional argument: 'values' 에러 발생.
log('내 숫자는', [1,2])