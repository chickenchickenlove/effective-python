from time import sleep
from datetime import datetime


# 키워드 인자의 값은 Import 시점에 단 한번만 평가됨.
# 따라서 같은 인자를 사용하게 됨.
def log(message, when=datetime.now()):
    print(f'{when}: {message}')


log('안녕')
sleep(0.1)
log('다시 안녕!')

# 실행 결과 (같은 초가 나오는 것을 볼 수 있음)
# 2023-10-16 18:30:35.765205: 안녕
# 2023-10-16 18:30:35.765205: 다시 안녕!

