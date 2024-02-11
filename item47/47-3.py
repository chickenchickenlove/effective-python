# 상속 구조에서도 __getattr__()를 이용해서 값을 얻어올 수 있음.
# 이 때, 무한재귀를 피하기 위해 super().__getattr__()로 호출하게 됨.

class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f'{name}를 위한 값'
        setattr(self, name, value)
        return value

class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f'* 호출: __getattr__({name!r})',
              f'인스턴스 딕셔너리 채워 넣음')
        result = super().__getattr__(name)
        print(f'* 반환: {result!r}')
        return result


data = LoggingLazyRecord()
print(f'이전: {data.__dict__}')
print(f'foo: {data.foo}')
print(f'이후: {data.__dict__}')

# 이전: {'exists': 5}
# * 호출: __getattr__('foo') 인스턴스 딕셔너리 채워 넣음
# * 반환: 'foo를 위한 값'
# foo: foo를 위한 값
# 이후: {'exists': 5, 'foo': 'foo를 위한 값'}