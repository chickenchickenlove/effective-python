# 그러나 이 방식은 다중 상속의 경우, 부모 클래스가 여러 번 호출된다는 문제가 있음. (특히 다이아몬드 상속에서 문제)
# 이런 형태로 의도치 않게 여러 번 호출되는 경우, 개발자가 알기 어려워 짐.

class MyBaseClass:
    def __init__(self, value):
        print(f'MyBaseClass __init__() : {value}')
        self.value = value

class TimeTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 2

class PlusFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 5

class ThisWay(TimeTwo, PlusFive):
    def __init__(self, value):
        TimeTwo.__init__(self, value)
        PlusFive.__init__(self, value)

foo = ThisWay(5)
for klass in ThisWay.mro():
    print(klass)
# print(ThisWay.mro())
print(f'(5 + 5) * 2 = 20이 나와야 하지만 실제로는 {foo.value}')
#