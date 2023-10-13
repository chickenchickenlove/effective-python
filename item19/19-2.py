numbers = [1,2,3,4,5]
def get_stats(numbers) -> tuple(int, int, int, int, int):
    maximum, minimum, avg, med, count = numbers
    return maximum, minimum, avg, med, count

# 제대로 된 값을 받았을 때
maximum, minimum, avg, med, count = get_stats(numbers)

# 잘못 사용했을 때. -> 같은 타입이라 값이 바뀌기 딱 좋다.
count, minimum, avg, med, maximum = get_stats(numbers)

# 줄바꿈도 가지각색이라 가독성이 안 좋음.
count, minimum, avg, med, maximum \
    = get_stats(numbers)

(count, minimum, avg, med, maximum) = get_stats(
    numbers)