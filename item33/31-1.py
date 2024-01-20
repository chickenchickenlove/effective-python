

def get_generator():
    k = list(range(10))
    for v in k:
        yield v


def generator():
    for v in ["a", "b", "c"]:
        yield v
    yield from [1, 2, 3]
    yield from (4, 5, 6)
    yield from range(7, 11)
    yield from get_generator()

gt = generator()
while (n := next(gt)) is not None:
    print(n)
