
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 아래 리스트 컴프리헨션은 문법적으로 차이가 있지만, 둘다 동일한 결과를 나타냄.
# 루프문 1개 + 조건문 1개라서 읽기 쉬움.
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]


# 문제가 되는 경우.
# 루프문 2개, 조건문 2개. 코드는 짧지만 읽기가 매우 어렵다.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]

# 이렇게 쓰는게 훨씬 낫다.
def choose_x3(l):
    return [x for x in l if x % 3 == 0]

filtered_improved = [choose_x3(row) for row in matrix if sum(row) >= 10]