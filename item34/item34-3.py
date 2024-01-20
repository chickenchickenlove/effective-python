# 제네레이터에 send()로 동적으로 Amplitude를 제공하면 가변 진동을 그릴 수 있게 되었음.
# 그런데 문제점은 읽기가 어렵다.
# 제네레이터를 조합하면 할수록 더 읽기 어려워지고 고려해야 할 부분이 많아진다.
# 이 경우, 각 자식 제네레이터가 끝나고 다름 제네레이터로 넘어가는 시점에 send()로 보내지는 입력이 하나씩 무시되게 된다.
# 아래 것은 다음과 같이 동작함.
# 1. None -> 첫번째 자식 제네레이터 yield까지 들어감.
# 2. 7 -> 첫번째 자식 제네레이터에 amplitude까지 들어감
# 3. [7, 6, 5]는 첫번째 자식 제네레이터에 amplitude로 사용됨.
# 4. send(4)를 하면, 첫번째 자식 제네레이터에서 StopIteration 발생하고, 다음 자식 제네레이터의 yield까지 넘어감.
#    즉, 4는 amplitude의 초기값으로 사용되지 않고 버려짐.
# 5. send(3)을 하면, 두번째 자식 제네레이터에서 초기값으로 사용됨.
# 이처럼 코드를 읽기가 어려워진다.

import math

def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    print('here')
    amplitude = yield # 초기 진폭을 받음.
    print(f'init amplitude = {amplitude}')
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        print(f'{amplitude=}')
        amplitude = yield output # 다음 진폭을 받음.
    print(f'last amplitude = {amplitude}')


def transmit(output):
    if output is None:
        print(f'출력: None')
    else:
        print(f'출력: {output:>5.1f}')


def run_modulating(it):
    amplitudes = [None, 7, 6, 5, 4, 3, 2, 1, 100, 90, 80, 70]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)

def complex_wave_modulating():
    yield from wave_modulating(3)
    print(1)
    yield from wave_modulating(4)
    print(2)
    yield from wave_modulating(5)
    print(3)


run_modulating(complex_wave_modulating())

