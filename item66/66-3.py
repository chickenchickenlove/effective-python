# contextlib안의 데이터가 필요한 경우, yield로 반환하면 with 절에서 사용할 수 있다.
import contextlib
import random

@contextlib.contextmanager
def get_random_number():
    try:
        yield random.randint(1, 100)
    finally:
        print('end context')


with get_random_number() as num:
    print(num)