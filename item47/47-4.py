# 1. 어트리뷰트에 접근할 때 마다 __getattribute__() 메서드가 호출됨.
# 2. 무한재귀를 막기 위해 super().__getattribute__()를 이용함.
# 3. 프로퍼티에 접근했을 때 없는 경우, AttributeError가 발생함. 이걸 잡아서 처리할 수도 있음. 그냥 놔두면 __getattr__()이 호출됨.


class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print(f'* 호출: __getattribute__({name!r})')
        try:
            value = super().__getattribute__(name)
            print(f'* {name!r} 찾음, {value!r} 반환')
            return value
        except AttributeError:
            value = f'{name}를 위한 값'
            print(f'* {name!r}를 {value!r}로 설정')
            setattr(self, name, value)
            return value

data = ValidatingRecord()
print(f'이전: {data.__dict__}')
print(f'foo: {data.foo}')
print(f'이후: {data.__dict__}')
