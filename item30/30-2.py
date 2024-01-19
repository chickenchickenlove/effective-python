# 제네레이터 함수가 호출되면, 이터레이터를 반환함.
# 이터레이터를 next()로 호출하면, yield 시점까지 진행 후 결과를 반환함.
# 다시 next()를 호출하면 yield 다음부터 작업을 진행함.
# 1. 결과를 리스트로 반환하는 것은 상대적으로 잡음이 존재함. → Result를 사용하지 않아서 상대적으로 더 읽기 편해짐.
# 2. 결과를 리스트에 모아서 반환하기 때문에 그만큼 작업 메모리가 필요함. → 제네레이터 내부에서 yield 시점에 사용하는 가장 큰 메모리가 제네레이터 사용의 전체 메모리임.

def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = '컴퓨터(영어: Computer, 문화어: 콤퓨터 , 순화어: 전산기)는 진공관'
it = index_words(address)

print(next(it))
print(next(it))
print(next(it))

# print(result[:-1])