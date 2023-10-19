# nonlocal은 가급적이면 사용하지 마라.
# nonlocal로 선언된 부분 ↔ 실제 변수가 사용되는 시점이 멀어지면, 이해하기 어려워진다.
def sort_priority(values, group):
    found = False
    def helper(x):
        nonlocal found # found는 지역변수가 아니라 자유변수임을 알려줌.
        if x in group:
            found = True
            return 0,x
        return 1,x
    values.sort(key=helper)
    return found

n = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
print(sort_priority(n, group))





