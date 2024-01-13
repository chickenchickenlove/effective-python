# 컴프리헨션 내부에 제어 하위 식은 2개까지만 사용 가능

# 1. 루프문 2개만 사용
# 2. 컴프리헨션 루프문 2개는 왼쪽 -> 오른쪽으로 순서대로 실행됨.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]

# 컴프리헨션 루프문 2개
squared = [[x**2 for x in row] for row in matrix]


# 3개짜린 쓰지마라.
my_list = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]

# 루프문 3개가 들어갔음. 읽기 어렵고, 길다.
flat2 = [x for sublist1 in my_list for sublist2 in sublist1 for x in sublist2]

# 대신에 이런 식으로 쓰는게 더 낫다.
flat3 = []
for sublist1 in my_list:
    for sublist2 in sublist1:
        flat3.extend(sublist2)





