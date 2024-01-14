# KeyError를 이용하는 방법
counters = {
    'a': 1,
    'b': 2
}

key = 'q'
try:
    counters[key] += 1
except KeyError as _:
    counters[key] = 1

