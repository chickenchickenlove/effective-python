# send()를 이용하면 문법도 따로 공부해야하고, 다른 키워드와 함께 사용되었을 때 너무 읽기 어려워진다.
# 따라서 send()를 사용하지 않고, 가변으로 줘야하는 경우 이터레이터를 전달하는 것이 훨씬 읽기 편하다.
# 1. 이터레이터는 상태를 가지고 있기 때문에 공유 가능하다는 점. (이어서 할 수 있음.)
# 2. 하지만 이터레이터 자체는 쓰레드 안전하지 않기 때문에, 조심해야한다는 점.

import math


def wave_modulating(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        yield next(amplitude_it) * fraction


def transmit(output):
    if output is None:
        print(f'출력: None')
    else:
        print(f'출력: {output:>5.1f}')


def run_modulating():
    amplitudes = [7, 6, 5, 4, 3, 2, 1, 100, 90, 80, 70, 1000]
    it = iter(amplitudes)
    for v in complex_wave_modulating(it):
        transmit(v)


def complex_wave_modulating(it):
    yield from wave_modulating(it, 3)
    yield from wave_modulating(it, 4)
    yield from wave_modulating(it, 5)


run_modulating()
