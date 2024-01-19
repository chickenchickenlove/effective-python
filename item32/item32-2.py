
# 앞서 이야기 한 메모리 문제를 해결하기 위해, 컴프리헨션을 ()로 실행한다.
# 반환값은 제네레이터가 된다. (이터레이터)
# 따라서 효율적으로 메모리를 사용할 수 있음.
# >>> <generator object <genexpr> at 0x0000026C33D74200>
it = (len(x) for x in open('my_file.txt'))
print(it)