# 제네레이터에 send()로 동적으로 Amplitude를 제공하면 가변 진동을 그릴 수 있게 되었음.
# 그런아 문제점은 읽기가 어렵다.
# 1. send()의 첫번째는 제네레이터의 yield까지 가기 전까지 진행되므로 반드시 None을 줘야한다는 점.
# 2. send()로 하면 첫번째 입력과 나머지 입력이 다르다는 점. (이걸 고려해서 코드를 작성해야 함)
# 3. 일반적인 이터레이팅 문법이 아니라는 점. send()로 이터레이팅을 하니까.

import math


def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield # 초기 진폭을 받음.
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output # 다음 진폭을 받음.


def transmit(output):
    if output is None:
        print(f'출력: None')
    else:
        print(f'출력: {output:>5.1f}')


def run_modulating(it):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)


run_modulating(wave_modulating(12))
