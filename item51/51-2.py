# 메타클래스는 Import 되는 시점에 __new__를 통해서 호출됨.
# 메타 클래스를 이용하면 잘 동작하기는 함. 그러나 아래 문제가 있음.
# 1. 상위 클래스가 메타 클래스를 적용한 경우, 하위 클래스에서 다시 한번 메타클래스를 사용하면 메타클래스 충돌이 일어남. (51-3.py 참고)
# 2. 1번 문제는 하위 클래스의 메타 클래스가 상위 클래스의 메타 클래스를 상속 받도록 하면 되지만, 라이브러리 코드인 경우 불가능함. (51-4.py 참고)
# 이 문제를 해결하기 위해 클래스 데코레이터를 사용.

import types
from functools import wraps

trace_types = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MethodDescriptorType,
    types.ClassMethodDescriptorType)

class TraceMeta(type):

    def __new__(meta, name, bases, class_dict):
        klass = super().__new__(meta, name, bases, class_dict)

        for key in dir(klass):
            value = getattr(klass, key)
            if isinstance(value, trace_types):
                wrapped = trace_func(value)
                setattr(klass, key, wrapped)

        return klass

def trace_func(func):

    # 단 한 번만 데코레이터를 적용함.
    if hasattr(func, 'tracing'):
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            result = e
            raise
        finally:
            print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')

    wrapper.tracing = True
    return wrapper


class TraceDict(dict, metaclass=TraceMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        return super().__getitem__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        super().__setitem__(*args, **kwargs)


trace_dict = TraceDict([('안녕', 1)])
trace_dict['거기'] = 2
trace_dict['안녕']
try:
    trace_dict['존재하지 않음']
except KeyError:
    pass