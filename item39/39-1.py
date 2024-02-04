
# 아래 코드는 클래스를 이어주기 위해 만들어진 함수가 제네릭 하지 않다.
# 함수가 제네릭 하지 않으면 재사용성이 떨어진다.
# 이 함수들(generate_inputs, create_workers)는 왜 Generic 하지 않은 것일까?
# 1. generate_inputs()에는 명시적으로 PathInputData를 사용함.
# 2. create_workers()는 명시적으로 LineCountWorker를 사용함.
# 이런 함수들은 사실상 하드 코딩 되어있는 것이나 다름없기 때문에 확장성이 부족함.
# 이의 개선을 위해서 '클래스 다형성'을 이용해 볼 수 있음.


import os
from threading import Thread



class InputData:
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()


class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):

    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        # 명시적으로 PathInputdata를 사용함. Generic 하지 않음
        yield PathInputData(os.path.join(data_dir, name))

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        # 명시적으로 LineCountWorker를 사용함. Generic 하지 않음.
        workers.append(LineCountWorker(input_data))
    return workers



def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, *rest = threads
    for worker in rest:
        first.reduce(worker)
    return first.result

def map_reduce(data_dir):
    input_list = generate_inputs(data_dir)
    workers = create_workers(input_list)
    return execute(workers)

