# 클래스 전체에 데코레이터를 추가하고 싶은 경우가 있음.
# 가장 간단한 형태는 아래와 같음. 그러나 아래 코드는 몇 가지 문제가 있음.
# 1. 불필요한 중복으로 가독성이 나빠짐.
# 2. 몇 개 빼먹는 실수를 할 수도 있음.
# 3. 부모 클래스에 메서드가 추가되는 경우, 이 데코레이터가 추가 되지 않은 채 동작함.
# 메타 클래스를 이용해 해결할 수 있음.

from functools import wraps

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


class TraceDict(dict):

    @trace_func
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @trace_func
    def __getitem__(self, *args, **kwargs):
        return super().__getitem__(*args, **kwargs)

    @trace_func
    def __setitem__(self, *args, **kwargs):
        super().__setitem__(*args, **kwargs)


trace_dict = TraceDict([('안녕', 1)])
trace_dict['거기'] = 2
trace_dict['안녕']
try:
    trace_dict['존재하지 않음']
except KeyError:
    pass