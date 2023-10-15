def my_generator():
    for i in range(10):
        print('generator called.')
        yield i


def my_func(*args):
    print('here')

# generator를 가변 인수로 전달할 때는 *를 이용해 언패킹 해줘야 함.
my_func(*my_generator())