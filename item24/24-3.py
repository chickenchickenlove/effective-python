import json

# import 시점에 키워드 변수는 단 한번만 평가된다.
# 따라서 키워드 변수를 명시적으로 전달하지 않으면, 모두 동일한 default를 사용한다.

def decode(data, default={}):
    try:
        return json.load(data)
    except:
        return default

foo = decode('잘못된 데이터')
foo['stuff'] = 5
bar = decode('또 잘못된 데이터')
bar['meep'] = 1
q = decode('a', {})
w = decode('b')

print(f'{foo = }, {bar = }, {q = }, {w = }')
print(f'{(foo == bar) = }')
