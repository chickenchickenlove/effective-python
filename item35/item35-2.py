# Throw를 이용해서 Timer를 만들 수 있지만, 코드에 잡음이 많다.
# Reset / StopIteration을 각각 Catch 해야하기 때문에 내포되는 것이 너무 많음.
# > 3 틱 남음
# > 2 틱 남음
# > 1 틱 남음
# > 0 틱 남음

class Reset(Exception):
    pass


def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period


def announce(remaining):
    print(f'{remaining} 틱 남음')


def check_for_reset():
    pass


def run():
    it = timer(4)
    while True:
        try:
            # 리셋이 필요할 때마다, Reset을 호출한다.
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)

run()