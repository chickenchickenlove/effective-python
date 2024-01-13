class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
r1.ohms = 10e3
# Public Attribute로 사용하면, 연산할 때 좀 더 읽기 쉬워짐.
r1.ohms += 5e3


class VoltageResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistor(1e3)
print(f'이전: {r2.current:.2f} 암페어')
r2.voltage = 10
print(f'이후: {r2.current:.2f} 암페어')



class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'저항 > 0 이어야 합니다. 실제 값: {ohms}')
        self._ohms = ohms

r3 = BoundedResistance(1e3)
r3.ohms = 0





# super().__init__()를 호출해야 부모 인스턴스가 초기화 됨.
# 부모 인스턴스가 초기화 되지 않으면, 부모 클래스가 가지고 있는 인스턴스 attribute를 자식에게서 접근할 수 없음.
# self.ohms 등등
# super().__init__()를 이용하면 부모 인스턴스의 초기화 과정을 몰라도 되기 때문에 느스한 결합을 하게 되므로, 사용하는 것이 좋음.