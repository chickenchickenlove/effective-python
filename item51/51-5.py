# 클래스에 데코레이터를 단 것을 클래스 데코레이터라고 함.
# Import 시점에 클래스가 호출된 직후에 클래스 데코레이터가 호출됨.
# 이 기능을 활용하면 됨.

import types
from functools import wraps


def my_class_decorator(klass):
    print('데코레이터 펑션 호출')
    klass.extra_param = '안녕'
    return klass


@my_class_decorator
class MyClass:
    print('클래스 호출')
    pass

print('시작 전')
print(MyClass)
print(MyClass.extra_param)

