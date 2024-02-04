# 클래스 다형성은 어떻게 이용할 수 있을까?
# 파이썬에서는 생성자가 __init__() 하나 밖에 없다.
# 따라서 클래스 계층 구조에 있는 모든 클래스가 동일한 갯수의 파라메터를 가지도록 강제할 수 없다.
# 이것을 해결하기 위해 @classmethod를 도입해서, 클래스의 다형성으로 문제를 해결할 수 있다.

import os
from threading import Thread


class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_list):
        workers = []
        for input_data in input_list:
            workers.append(cls(input_data))
        return workers

class LineCountWorker(GenericWorker):

    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, *rest = threads
    for worker in rest:
        first.reduce(worker)
    return first.result

# map_reduce 함수는 worker 클래스, input 클래스를 전달받아서 class Method를 호출한다.
# 따라서, 이전에 LineWorker처럼 명시해서 하던 것과 비교했을 때 제네릭한 코드가 되었다.
def map_reduce(worker_class, input_class, config):
    input_list = input_class.generate_inputs(config)
    workers = worker_class.create_workers(input_list)
    return execute(workers)
