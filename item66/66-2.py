# 만약 특정 블록에서만 동적으로 디버깅 레벨을 바꾸고 싶다면, With 절을 사용할 수 있다.
# @contextlib.contextmanager를 사용하면 직접 __enter__, __exit__ 메서드를 구현할 필요없이 편리하게 with절을 사용할 수 있도록 해줌.
# 1. With절 시작 시, yield까지 실행되고 반환됨.
# 2. With절 끝날 때, yield부터 끝까지 실행됨.

import logging
import contextlib

logging.basicConfig()

@contextlib.contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


def my_function():

    logging.debug('디버깅 데이터')
    logging.error('이 부분은 오류 로그')
    logging.debug('추가 디버깅 데이터')

with debug_logging(logging.DEBUG):
    my_function()

my_function()

