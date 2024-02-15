# 믹스인의 장점은 간단히 사용할 수 있고, 필요할 때 다른 기능으로 오버라이드 해 변경할 수 있다는 점이다.
# 예를 들어 BinaryTreeWithParent는 이대로 사용하면 _traverse_dict()에서 무한 재귀가 발생한다.
# 이 부분을 해결하기 위해 ToDictMixin에서 제공하는 _traverse()를 Override해서 문제를 해결할 수 있다.

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


class BinaryTreeWithParent(BinaryTree):
    def __init__(self,
                 value,
                 left=None,
                 right=None,
                 parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent

    def _traverse(self, key, value):
        if (isinstance(value, BinaryTreeWithParent) and
            key == 'parent'):
            return value.value # 순환 참조 방지
        else:
            return super()._traverse(key, value)




root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
print(root.to_dict())