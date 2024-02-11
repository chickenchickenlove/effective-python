# 인스턴스의 어트리뷰트에 접근하면 항상 __getattribute__()가 호출됨.
# __getattribute__()에서 어트리뷰트를 찾을 수 없으면 __getattr__()이 호출됨.
# __getattr__()에서 setattr()로 인스턴스에 어트리뷰트를 동적으로 셋팅하고, 그 값을 반환할 수 있음.
# 즉, 이 메타 메서드를 이용하면 동적으로 인스턴스의 어트리뷰트를 추가할 수 있음.


class Hello:

    def __init__(self):
        self.hello = 'hello100'

    def __getattribute__(self, item):
        print('__getattribute__ called.')
        value = super().__getattribute__(item)
        return value

    def __getattr__(self, item):
        print('__getattr__ called.')
        value = f'{item}을 위한 값'
        setattr(self, item, value)
        return value

h = Hello()
print(h.hello)
print(h.a)



