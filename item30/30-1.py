# 1. 결과를 리스트로 반환하는 것은 상대적으로 잡음이 존재함.
# 2. 결과를 리스트에 모아서 반환하기 때문에 그만큼 작업 메모리가 필요함.

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

address = '컴퓨터(영어: Computer, 문화어: 콤퓨터 , 순화어: 전산기)는 진공관'
result = index_words(address)
print(result[:-1])

