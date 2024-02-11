# 배경 지식
# 1. 클래스/인스턴스 어트리뷰트에 접근하면 __getattribute__() 가 호출됨.
# 2. __getattribute__()에서 찾을 수 없는 경우 __getattr__()이 호출됨.
# 3. __getattr__()에서 어트리뷰트에 기본 값을 설정하고, 그 값을 반환할 수 있음.

class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f'{name}를 위한 값'
        setattr(self, name, value)
        return value

data = LazyRecord()
print(f'이전: {data.__dict__}')
print(f'foo: {data.foo}')
print(f'이후: {data.__dict__}')


# 이전: {'exists': 5}
# foo: foo를 위한 값
# 이후: {'exists': 5, 'foo': 'foo를 위한 값'}