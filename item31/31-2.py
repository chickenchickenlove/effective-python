# 만약 2번 이터레이팅 해야하는 함수 + 인풋이 제네레이터라면,
# 아래 함수는 원하는 출력이 나오지 않는다.
# 기대값 >>> [11.538461538461538, 26.923076923076923, 61.53846153846154]
# 실제값 >>> []

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def get_visits():
    for v in [15, 35, 80]:
        yield v


visits = get_visits()
percentages = normalize(visits)
print(percentages)


