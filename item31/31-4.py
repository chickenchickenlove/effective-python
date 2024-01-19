# 이터레이터를 생성하는 함수를 전달해서 필요할 때 마다 사용함.
# 그러나 이터레이터를 생성하는 '함수'를 인자로 전달하는게 보기 좋지 않음.
# 기대값 >>> [11.538461538461538, 26.923076923076923, 61.53846153846154]
# 실제값 >>> [11.538461538461538, 26.923076923076923, 61.53846153846154]

def normalize(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


def get_visits():
    visits = [15, 35, 80]
    for v in visits:
        yield v


visits = get_visits
percentages = normalize(visits)
print(percentages)
