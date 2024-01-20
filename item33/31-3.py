# 한 제네레이터 안에서 여러 제네레이터를 호출하는 것이 가독성 관점에서 떨어짐.
# 이의 개선을 위해 yield from을 사용할 수 있음.
# 여러 for 문이 반복되는 것을 개선했고, 선언되는 변수 자체도 줄여서 이해하기 쉬워짐.

def move(period, speed):
    for _ in range(period):
        yield speed


def pause(delay):
    for _ in range(delay):
        yield 0


def animate():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)


for delta in animate():
    print(f'Delta: {delta:.1f}')

