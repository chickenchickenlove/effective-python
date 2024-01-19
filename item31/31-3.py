# 이전 문제를 해결하기 위해 이터레이터의 내용 전체를 복사해서 사용해 볼 수 있음.
# 리스트를 하나로 만드는 것이기 때문에 제네레이터를 사용하는 의미가 없어짐. (메모리 절감)
# 기대값 >>> [11.538461538461538, 26.923076923076923, 61.53846153846154]
# 실제값 >>> [11.538461538461538, 26.923076923076923, 61.53846153846154]

def normalize_defensive(numbers):
    numbers_copy = list(numbers) # 방어적 복사
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result


def get_visits():
    for v in [15, 35, 80]:
        yield v


visits = get_visits()
percentages = normalize_defensive(visits)
print(percentages)


