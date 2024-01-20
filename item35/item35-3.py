# Throw를 이용해서 Timer를 만들 수 있지만, 코드에 잡음이 많다.
# Reset / StopIteration을 각각 Catch 해야하기 때문에 내포되는 것이 너무 많음.
# -> 이 부분을 해결하기 위해 상태가 있는 컨테이너를 제공하고 StateTransition을 구현하는 것이 낫다.
# -> 컨테이너 객체를 만들고, 상태 변화를 할 수 있는 함수를 제공.
# -> it.throw()로 에러를 주입하는 대신, 명시적으로 timer.reset() 호출
# -> __iter__()를 구현해서 컨테이너 객체를 생성해서, for 문을 돌리면서 StopIteration 에러까지 자동처리하기.


class Timer:

    def __init__(self, period):
        self.period = period
        self.current = period

    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current


def announce(remaining):
    print(f'{remaining} 틱 남음')


def check_for_reset():
    pass


def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)


run()