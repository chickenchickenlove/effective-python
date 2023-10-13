lengths = [1, 2, 3, 4]


def get_avg_ratio(numbers: list[int]):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

# 언패킹을 이용하라.
longest, *middle, shortest = get_avg_ratio(lengths)





