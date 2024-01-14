def get_batches(count, size):
    return count // size

stock = {
    'a': 125,
    'b': 35,
    'c': 8,
    'd': 24,
}

order = ['a', 'b', 'c']


# 첫번째 경우는 리스트 컴프리헨션에서 2개의 식으로 더 명확히 표현할 수 있음.
result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches


# 리스트 컴프리헨션 내에서 식 2개 내포해서 처리할 수 있음.
# 그러나 get_batches()라는 값이 동일한 곳에서 사용되기 때문에 실수하기 쉬움. (수정이 필요한 경우 2개 동시에 수정해야 하는데, 1개만 수정한다거나)...
result = {name: get_batches(stock.get(name, 0), 8)
          for name in order if get_batches(stock.get(name, 0), 8)}


# 왈러스 연산자를 이용해, get_batches()를 줄임. 따라서 실수할 가능성도 줄이고, 가독성을 더 올림.
result1 = {name: batches
           for name in order if (batches := get_batches(stock.get(name, 0), 8))}


# stock.get() 자체가 노이즈를 가져오기 때문에 이를 개선한 버전임.
name_count = [(name, stock.get(name, 0)) for name in order]
result2 = {name: batches for name, count in order if (batches := get_batches(count, 8))}
