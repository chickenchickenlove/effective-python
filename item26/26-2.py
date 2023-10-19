# 데코레이터를 사용하더라도 기존 함수의 이름, doc이 잘 전달될 수 있도록
# 다음 명령어를 사용하자.
import functools

def deco(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        print('here')
        return func(*args, **kwargs)
    return wrapper_func


@deco
def hello():
    print('hello')
    return 1

print(hello.__name__)