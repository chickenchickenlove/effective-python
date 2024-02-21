# With 절에서 변수를 함께 사용하는 것은 특별한 문맥적 의미를 가지기도 한다.
# With 절에서 제공되는 변수는 With절 문맥 내에서만 한정된다는 특별한 의미를 가짐.
# 결론적으로 With절의 안/밖은 서로 다른 문맥을 가지고, 격리시킬 수 있음을 의미함.

import logging
import contextlib

logging.basicConfig()

@contextlib.contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug(f'대상: {logger.name}!')

logger = logging.getLogger('my-log')
logger.debug('디버그 메세지는 출력되지 않습니다.')
logger.error('오류 메세지는 출력됩니다.')