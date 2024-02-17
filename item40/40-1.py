# "클래스_이름".__init__()로 직접 부모 클래스의 초기화를 호출할 수 있음.

class MyBaseClass:
    def __init__(self, value):
        print(f'MyBaseClass __init__() : {value}')
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self, value):
        print(f'MyChildClass __init__() : {value}')
        MyBaseClass.__init__(self, value)


MyChildClass(5)
