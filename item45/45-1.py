from datetime import datetime, timedelta

# 이렇게 구현된 경우, Bucket으로부터 '불가능함' 응답을 받았을 때, 두 가지 경우가 있는데 무엇인지 알 수 없음.
# 1. 주기 내에 버킷에 할당된 용량을 다 쓴 경우
# 2. 주기가 지났는데, 버킷에 용량이 다시 리필되지 않아서 할 수 없는 경우.
# 이런 부분을 구별하는 부가기능을 추가하고 싶다면, quota를 @property를 이용해 확장할 수 있음.
# 이 때 사용자의 코드는 전혀 변하지 않음.
class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return f'Bucket(quota={self.quota})'


def fill(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount

def deduct(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False # 새 주기가 시작되었는데, 아직 버킷 할당량이 재설정되지 않음.
    if bucket.quota - amount < 0:
        return False # 버킷의 가용 용량이 충분하지 못하다.
    else:
        bucket.quota -= amount
        return True # 버킷의 가용 용량이 충분하므로 필요한 분량을 사용한다.


bucket = Bucket(60)
fill(bucket, 100)
print(bucket)

if deduct(bucket, 99):
    print('99 용량 사용')
else:
    print('가용 용량이 작아서 99 용량을 처리할 수 없음.')
print(bucket)

if deduct(bucket, 3):
    print('3 용량 사용')
else:
    print('가용 용량이 작아서 3 용량을 처리할 수 없음.')
print(bucket)
