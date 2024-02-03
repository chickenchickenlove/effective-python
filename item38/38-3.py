# 클로저를 이용한 상태가 있는 함수를 제공하는 것보다는 인터페이스를 사용하는 것이 가독성이 더 좋다.
# 그러나 Counter 클래스 그 자체는 무엇인지 의미하는 바를 알기 어렵다.
# 1. 처음 보는 사람이 이 클래스를 보았을 때, 어디에 쓰는지 명확히 알 수 없다.
# 예를 들면 missing() 메서드는 어떤 것을 위해서 사용해야할까? 등등.
# 인스턴스를 callable로 만드는 방법이 더 좋을 것이다.
from collections import defaultdict

class CounterMissing:

    def __init__(self):
        self.count = 0

    def missing(self):
        self.count += 1
        return 0

current = {'초록': 12, '파랑': 3}
increments = [
    ('빨강', 5),
    ('파란', 17),
    ('주황', 9)
]

counter = CounterMissing()
result = defaultdict(counter.missing, current)
print(f'이전 : {dict(result)}')
for key, amount in increments:
    result[key] += amount
print(f'이후 : {dict(result)}')


