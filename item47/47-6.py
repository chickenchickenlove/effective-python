# 1. 어트리뷰트에 값을 대입할 때 마다 __setattr__()이 호출됨.
# 2. 무한 재귀를 막기 위해 super().__setattr__()을 호출하도록 함.

class SavingRecord:

    def __setattr__(self, key, value):
        print('set attr 호출')
        super().__setattr__(key, value)


a = SavingRecord()
a.q = 10

# set attr 호출