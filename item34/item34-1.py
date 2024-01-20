# 현재 코드는 단방향으로 입력이 들어가는 제네레이터를 사용하고 있다.
# 이 경우, 제네레이터에 동적인 입력을 넣어서 처리할 수가 없다.
# 아래 코드는 Sin / Cos의 주파수를 발생시켜주는 코드인데, 만약 진폭을 수정해서 가변적인 그래프를 그리고 싶다면 어떻게 해야할까?

import math

def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output


def transmit(output):
    if output is None:
        print(f'출력: None')
    else:
        print(f'출력: {output:>5.1f}')


def run(it):
    for output in it:
        transmit(output)


run(wave(3.0, 8))




