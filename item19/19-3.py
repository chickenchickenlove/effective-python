# 19-2의 문제점 해결
from dataclasses import dataclass

numbers = [1,2,3,4,5]

@dataclass
class ReturnValue:
    maximum: int
    minimum: int
    avg: int
    med: int
    count: int

def get_stats(numbers: list[int]) -> ReturnValue:
    maximum, minimum, avg, med, count = numbers
    return ReturnValue(maximum, minimum, avg, med, count)

ReturnValue = get_stats(numbers)

# 필드로 접근할 수 있음.
print(ReturnValue.maximum)

