# defaultdict에 Key Missing이 발생했을 때, 리턴되는 값을 정의하고 싶음.
# defaultdict는 defaulFactory라는 파라메터로 Hook을 제공한다. (위 기능)
# 이 때, log_missing 함수를 전달하면 Key가 없을 때 마다 다음 작업이 발생함.
# 1. Key에 0이라는 값이 추가됨.
# 2. '키 추가됨'이 출력됨.
# 이처럼 Hook 인터페이스에는 상태가 없는 함수를 손쉽게 추가할 수 있음.
# 클래스를 정의하는 것보다 함수 하나만 정의하는 것이 더 쉽기 때문이다.

from collections import defaultdict

def log_missing():
    print('키 추가됨')
    return 0


current = {'초록': 12, '파랑': 3}
increments = [
    ('빨강', 5),
    ('파란', 17),
    ('주황', 9)
]

result = defaultdict(log_missing, current)
print(f'이전 : {dict(result)}')
for key, amount in increments:
    result[key] += amount
print(f'이후 : {dict(result)}')





