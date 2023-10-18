def remainder(number, divisor, hello):
    print(hello)
    return number % divisor


print(remainder(5, 20, 20))
print(remainder(5, 20, hello=9000))

# 위치 기반으로 divisor=20이 되어있음. 다시 divisor = 7을 하면 중복으로 오류남.
print(remainder(5, 20, divisor=7))

# 전부 다 키워드를 기반으로 사용할 때는 순서 문제 없음.
print(remainder(hello=5, divisor=20, number=9))