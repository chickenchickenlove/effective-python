# Generator를 사용할 때, throw()를 이용해서 양방향 통신을 할 수도 있다.
# 아래와 같이 사용할 수 있음.


class MyError(Exception):
    pass

def my_generator():
    yield 1
    try:
        yield 2
    except MyError as e:
        print(f'MyError 발생. {e}')
    else:
        yield 3
    yield 4

it = my_generator()
print(next(it))
print(next(it))
print(it.throw(MyError("test error")))
print(next(it))




