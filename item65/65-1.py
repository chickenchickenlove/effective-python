import json

def load_json_key(data, key):
    try: # 예외가 반드시 발생할 수 있는 부분을 나타냄.
        print('* JSON 데이터 읽기')
        result_dict = json.loads(data)
    except ValueError as e:
        print('* ValueError 처리')
        raise KeyError(key) from e # ValueError가 발생할 수 있음.
    else:
        # 예외가 발생하지 않는 부분을 나타냄.
        print('* 키 검색')
        return result_dict[key] # KeyError가 발생할 수 있음.


data = '{"foo": "bar",}'
key = 'foo'

try:
    'bar' == load_json_key(data, key)
except KeyError as e:
    print(f"Caught an error: {e}")
    if e.__cause__:
        print(f"Original cause: {e.__cause__}")