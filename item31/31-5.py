# '제네레이터 생성 함수' 전달이 보기 좋지 않기 때문에 이터레이터 프로토콜을 구현한 객체를 전달. (그것이 새로운 컨테이너 클래스임)
# for v in values -> iter(values) -> values.__iter__() 순서대로 호출됨.
# 이 때, __iter__()가 이터레이터 객체를 반환하기만 하면 '이터레이터 프로토콜'을 만족함.
# 이터레이터 프로토콜을 만족하는 객체는 이터레이팅 할 수 있음.
# 한 가지 문제점은 다음과 같음.
# iter()에 이터레이터가 전달되면, 이터레이터 객체가 그대로 반환됨.
# iter()에 컨테이너 타입이 전달되면, 새로운 이터레이터 객체가 반환됨.
# 그런데 numbers가 컨테이너, 혹은 이터레이터 프로토콜을 구현한 새로운 컨테이너 클래스를 제공하면 한 메서드에서 여러번 이터레이팅 가능한.ㅁ
# 그러나 이터레이터 그 자체를 전달하는 경우, 문제가 발생할 수 있음.


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


class ReadVisits:

    def __init__(self):
        self.visits = [15, 35, 80]

    def __iter__(self):
        for v in self.visits:
            yield v


visits = ReadVisits()
percentages = normalize(visits)
print(percentages)
