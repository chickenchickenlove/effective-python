# 다이아몬드 상속에서 부모클래스 초기화가 여러번 되는 것을 막기 위해 다음을 사용할 수 있음.
# 1. super().__init__()로 초기화한다.
# 2. super().__init__()는 각 클래스가 가지고 있는 mro(표준 메서드 결정 순서)에 따라서 순차적으로 부모 클래스를 초기화함.
# 3. 따라서 공통 부모 클래스가 단 한번만 초기화 된다.
# 4. 실행되는 순서는 mro()인데, 코드 블락은 반대로 처리된다.
#    Thisway init() -> TimeTwo init() -> PlusFive init() -> MyBassClass init() 및 init() 블록 처리 -> PlusFive init() 블록 처리 -> TimeTwo init() 블록 처리 -> Thisway init() 블록 처리

class MyBaseClass:
    def __init__(self, value):
        print(f'MyBaseClass __init__() : {value}')
        self.value = value

class TimeTwo(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        print(1)
        self.value *= 2

class PlusFive(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        print(2)
        self.value += 5

class ThisWay(TimeTwo, PlusFive):
    def __init__(self, value):
        super().__init__(value)

foo = ThisWay(5)
for m in ThisWay.mro():
    print(m)
print(f'(5 + 5) * 2 = 20이 나와야 하지만 실제로는 {foo.value}')
