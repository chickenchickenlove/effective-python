# 현재 이 상태에서는 Error 레벨의 로그만 찍힌다.

import logging

logging.basicConfig()

def my_function():
    logging.debug('디버깅 데이터')
    logging.error('이 부분은 오류 로그')
    logging.debug('추가 디버깅 데이터')

my_function()