# 부모 클래스의 Attribute를 불변으로 만들기.
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        # self = FixedResistance임
        # FixedResistance는 self.ohms를 Attribute로 가짐. (부모가 init 하니까)
        # 부모가 init 하는 시점에는 self.ohms가 초기화 되어 있지 않은 상태에서 이 메서드가 호출되기 때문에 self._ohms = ohms로 처리함.
        # 그 이후에는 self.ohms가 초기화 되었기 때문에 항상 에러를 발생시킴.
        if hasattr(self, 'ohms'):
            raise AttributeError(f'Ohms는 불변 객체입니다.')
        self._ohms = ohms


r = FixedResistance(1e3)
r.ohms = 0
