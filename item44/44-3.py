class Resistor:
    def __init__(self, ohms):
        # 공개 Attribute로 시작했다가, 이 녀석이 Setter를 호출하는 형태가 되어버림. (확장에 유리함)
        # 그러나 잘 모른다면, 이해는 어려울 듯?
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


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


# super().__init__(ohms) -> self.ohms 여기서, @property가 호출됨. -> @ohms.setter가 호출됨.
r3 = BoundedResistance(1e3)
print(r3.ohms)
r3.ohms = 0