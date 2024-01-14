# get를 이용하는 방법
counters = {
    'a': 1,
    'b': 2
}

key = 'q'

count = counters.get(key, 0) + 1
counters[key] = count

