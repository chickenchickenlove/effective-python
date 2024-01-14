# 컴프리헨션에서 왈러스 연산자를 사용하면, 변수가 외부 Scope으로 유출됨.
# 컴프리헨션 내부의 조건식 / 일반식에서도 동일하게 노출됨.

stock = {'a': 10, 'b': 20}

half = [(last := count // 2) for count in stock.values()]
print(f'{last=}')

half2 = [count for count in stock.values() if (last2 := count // 2)]
print(f'{last2=}')
