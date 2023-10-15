def log(seq, message, *values):
    if not values:
        print(f'{seq} - {message}')
    else:
        value_str = ', '.join(str(x) for x in values)
        print(f'{seq} - {message}: {value_str}')

# seq = 내 숫자는
# message = [1,2]
# 로 각각 인자가 잘못 전달됨.
log('내 숫자는', [1,2])