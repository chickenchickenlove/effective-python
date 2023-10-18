def remainder(number, divisor, hello):
    print(hello)
    return number % divisor


a = {
    'number': 10,
    'divisor': 20
    }

b = {'hello': 30}

print(remainder(**a, **b))

