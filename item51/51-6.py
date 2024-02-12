# 클래스 데코레이터를 이용하는 경우, 메타 클래스 충돌로부터 자유로워짐.
# 가독성 있는 코드로 사용할 수 있음.

import types
from functools import wraps

trace_types = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MethodDescriptorType,
    types.ClassMethodDescriptorType)


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

def trace(klass):
    for key in dir(klass):
        value = getattr(klass, key)
        if isinstance(value, trace_types):
            wrapped = trace_func(value)
            setattr(klass, key, wrapped)
    return klass

@trace
class TraceDict(dict):
    pass

trace_dict = TraceDict([('안녕', 1)])
trace_dict['거기'] = 2
trace_dict['안녕']
try:
    trace_dict['존재하지 않음']
except KeyError:
    pass