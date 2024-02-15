import json

# 믹스인끼리 합성해서 공통의 기능을 제공할 수도 있다.
# 믹스인 클래스 내에서 다음을 처리할 수도 있음.
# 1. @classmethod를 이용해서 클래스 레벨의 동작도 제공할 수 있음.
# 2. 일반 메서드를 이용해 인스턴스 레벨의 동작도 제공할 수 있음.


class ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        return {key: self._traverse(key, value) for key, value in instance_dict.items()}

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class JsonMixin:

    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())


class DatacenterRack(ToDictMixin, JsonMixin):
    def __init__(self, switch=None, machines=None):
        self.switch = switch
        self.machines = [
            Machine(**kwargs) for kwargs in machines]


class Switch(ToDictMixin, JsonMixin):
    def __init__(self, ports=None, speed=None):
        self.ports = ports
        self.speed = speed


class Machine(ToDictMixin, JsonMixin):
    def __init__(self, cores=None, ram=None, disk=None):
        self.cores = cores
        self.ram = ram
        self.disk = disk


serialized = """{
    "switch": {"ports": 5, "speed": 1e9}, 
    "machines": [
        {"cores": 8, "ram": 32e9, "disk": 5e12},
        {"cores": 4, "ram": 16e9, "disk": 1e12},
        {"cores": 2, "ram": 8e9, "disk": 500e9}
    ]
}"""

deserealized = DatacenterRack.from_json(serialized)
roundtrip = deserealized.to_json()
assert json.loads(serialized) == json.loads(roundtrip)