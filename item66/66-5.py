from threading import Lock


# 만약 With절을 사용하지 않으면 이런 코드를 작성해야 함.
# 1. lock.release()를 누락하기라도 하면 큰 문제가 생김.
# 2. try ~ finally가 많이 사용되면서 시각적 잡음이 생김.
lock = Lock()
lock.acquire()
try:
    print(1)
finally:
    lock.release()


# 컨텍스트 매니저를 사용하게 되면 위 단점이 모두 극복됨.
import contextlib

@contextlib.contextmanager
def get_lock():
    lock.acquire()
    try:
        yield
    finally:
        lock.release()

with get_lock():
    print(1)


