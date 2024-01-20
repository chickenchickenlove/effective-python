# 제네레이터 내에서 제네레이터를 여러 개 중복해서 사용하는 경우가 있을 수 있음.
# 이 때, 부모 제네레이터 내에서 자식 제네레이터를 여러번 사용하는 경우 다음 문제가 있음.
# 1. 동일한 문장이 여러번 사용됨. (for 문, yield 문)
# 2. 동일한 변수도 계속 선언됨(delta). 다른 경우라면, 여러 변수가 계속 선언되어야 할 수도 있음. (delta가 아니라 다른 의미를 가지는 변수라면). 즉, 문맥 파악이 어려워짐.
# 이런 이유 때문에 제네레이터 안에서 다른 제네레이터를 for문으로 호출하는 것은 가독성 관점에서 좋지 않다.

def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

for delta in animate():
    print(f'Delta: {delta:.1f}')

