def remainder(**kwargs):
    for k, v in kwargs.items():
        print(f'{k = }, {v = }')


a = {
    'number': 10,
    'divisor': 20
    }

print(remainder(hello='a', ballo="b", **a))

