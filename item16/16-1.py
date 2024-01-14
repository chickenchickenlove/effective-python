# in을 이용해서 처리하는 방법
counters = {
    'a': 1,
    'b': 2
}

key = 'q'

if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1