# 만약, 상태가 있는 함수를 Hook으로 사용하고 싶다면 클로저를 이용하면 된다.
# defaultdict에서 없는 키가 호출될 때 마다, missing() 함수가 호출된다.
# missing 함수가 호출될 때 마다 add_count 클로저 변수를 호출한다.
# 결과적으로 Missing Key가 몇번 있었는지를 클로저 변수를 이용해 저장한다.
# 즉, 상태를 저장하는 함수다.
# 상태를 저장하는 함수는 상태가 없는 함수에 비해 읽기 어렵다.
# 이런 경우 클로저 함수 대신, 클래스를 도입하는 것이 더 좋다.

from collections import defaultdict


def increment_with_report(current, increments):
    add_count = 0

    def missing():
        nonlocal add_count
        add_count += 1
        return 0

    result = defaultdict(missing, current)
    print(f'이전 : {dict(result)}')
    for key, amount in increments:
        result[key] += amount
    print(f'이후 : {dict(result)}')


current = {'초록': 12, '파랑': 3}
increments = [
    ('빨강', 5),
    ('파란', 17),
    ('주황', 9)
]
increment_with_report(current, increments)