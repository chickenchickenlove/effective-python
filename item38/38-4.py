# 클래스의 __call__ 메서드를 구현하면, 인스턴스는 callable 객체가 된다.
# 즉, 인스턴스()로 호출할 수 있게 됨.
# 이렇게 전달되는 인스턴스가 더 읽기 명확하다.
from collections import defaultdict

class CounterMissing:

    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return 0


current = {'초록': 12, '파랑': 3}
increments = [
    ('빨강', 5),
    ('파란', 17),
    ('주황', 9)
]

counter = CounterMissing()
result = defaultdict(counter, current)
print(f'이전 : {dict(result)}')
for key, amount in increments:
    result[key] += amount
print(f'이후 : {dict(result)}')


