# Getter를 잘못 쓴 경우
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class MysteriousResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        # Getter에서 다른 프로퍼티를 수정하면서 이상하게 됨.
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, 'ohms'):
            raise AttributeError(f'Ohms는 불변 객체입니다.')
        self._ohms = ohms


# super().__init__(ohms) -> self.ohms 여기서, @property가 호출됨. -> @ohms.setter가 호출됨.
r = MysteriousResistor(1e3)
r.ohms = 0
