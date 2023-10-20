# 짝수를 제곱한 값 구하기
a = [1, 2, 3, 4, 5, 6, 7, 8]

# 컴프리헨션 이용
even_squares = [x ** 2 for x in a if x % 2 == 0]

# map, filter 이용. 
even_squares_with_map = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, a)))