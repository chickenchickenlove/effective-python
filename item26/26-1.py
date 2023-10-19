# 데코레이터를 사용하면, 기존 함수의 이름과 __Docs__는 없어짐.
# 디버깅 시에 문제가 발생할 수 있음.
def deco(func):
    def wrapper_func(*args, **kwargs):
        print('here')
        return func(*args, **kwargs)
    return wrapper_func


@deco
def hello():
    print('hello')
    return 1

print(hello.__name__)