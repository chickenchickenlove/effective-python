def make_lemonade(count):
    pass

def out_of_stock():
    pass


fresh_fruits = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5
}

# count가 If 절에서만 사용되는데, 굳이 밖에 선언될 필요는 없음.
count = fresh_fruits.get('레몬', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()



