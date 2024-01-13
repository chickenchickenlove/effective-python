# 단순 Setter / Getter를 사용하는 경우, 복잡한 작업할 때 지저분 해보임.
# 그러나 Setter / Getter는 캡슐화, Validation등 다양한 부가기능을 추가할 수 있음.
# 그래서 필요할 것 같은데?
class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


r0 = OldResistor(50e3)
print(f'이전, {r0.get_ohms()}')
r0.set_ohms(10e3)
print(f'이후, {r0.get_ohms()}')


r0.set_ohms(r0.get_ohms() - 4e3)
assert r0.get_ohms() == 6e3