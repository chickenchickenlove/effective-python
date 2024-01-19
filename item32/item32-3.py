# 이터레이터를 두 개씩 연결해서 사용할 수 있음.
# 1. 그러나 각 이터레이터는 상태를 가지고 있기 때문에 다른 곳에서 재사용할 수는 없음.
# 2. 둘 중 하나의 이터레이터에 next()를 적용하면, 다른 이터레이터도 적용 받음.
#    it에 누군가 next()를 한번 적용하면, roots를 전체 이터레이팅 했을 때 한번은 값이 빠짐.
# <generator object <genexpr> at 0x000001ECE57D4200>
# <generator object <genexpr> at 0x000001ECE57D5D20>
# 27
# 19
# (15, 3.872983346207417)

it = (len(x) for x in open('my_file.txt'))
roots = ((x, x**0.5) for x in it)

print(it)
print(roots)
print(next(it))
print(next(it))
print(next(roots))
