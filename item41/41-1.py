
# 다중상속보다는 믹스인을 사용하는 것이 좋다.
# 다중상속으로 인해 발생할 수 있는 골치 아픈 경우를 제외할 수 있기 때문이다.
# 믹스인은 다음을 의미한다.
# 1. 믹스인은 자식 클래스가 사용할 메서드 몇 개만 정의하는 클래스임.
# 2. 믹스인은 __init__()도 구현하지 않음. (멤버 변수가 없음.)
# 믹스인은 제네릭한 기능을 제공하는데 사용할 수 있다.
# 믹스인을 계층화 / 합성해서 반복적인 코드를 최소화하고 재사용성을 늘릴 수 있다.


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

class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BinaryTree(10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)))
print(tree.to_dict())
