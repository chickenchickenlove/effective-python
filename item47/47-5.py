# hasattr()도 __getattibute__() -> __getattr__() 순으로 호출함.

class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f'{name}를 위한 값'
        setattr(self, name, value)
        return value

data = LazyRecord()
print(f'이전: {data.__dict__}')
print(f'최초에 foo가 있나:', hasattr(data, 'foo'))
print(f'이후: {data.__dict__}')
print(f'다음에 foo가 있나:', hasattr(data, 'foo'))

# 이전: {'exists': 5}
# * 호출: __getattr__('foo') 인스턴스 딕셔너리 채워 넣음
# * 반환: 'foo를 위한 값'
# foo: foo를 위한 값
# 이후: {'exists': 5, 'foo': 'foo를 위한 값'}