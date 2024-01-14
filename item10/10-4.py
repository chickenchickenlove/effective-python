def make_juice():
    pass


def pick_fruit():
    pass


# 무한 루프를 돌게 하고, 무한 루프를 끝내는 방법이 Break 밖에 없음.
# 잡음이 발생할 수 있는데, 이것을 왈러스 연산자로 개선할 수 있음.
# -> 왈러스 연산자를 이용하면 이 부분을 더 읽기 쉬워진다.
bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)