# "클래스_이름".__init__()로 직접 부모 클래스의 초기화를 호출할 수 있음.
# 아래 코드처럼 다중 상속을 하는 경우에도 부모 클래스 이름으로 직접 __init__()를 호출할 수 있음.

class MyBaseClass:
    def __init__(self, value):
        print(f'MyBaseClass __init__() : {value}')
        self.value = value

class TimeTwo:
    def __init__(self):
        self.value *= 2

class PlusFive:
    def __init__(self):
        self.value += 5

class OneWay(MyBaseClass, TimeTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimeTwo.__init__(self)
        PlusFive.__init__(self)


foo = OneWay(5)
print(f'첫 번째 부모 클래스 순서에 따른 값은 (5 * 2) + 5 = {foo.value}')
