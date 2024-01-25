# 학생 이름 - 과목 - (점수, 가중치)로 관리 중임.
# 이전 코드는 너무 많은 내포가 포함되어 있어, 사용하기도 어렵고 유지보수도 어려웠다.
# 1. 내장 자료구조가 내포된 것들을 클래스의 계층구조로 나타내는 것이 좋다. (읽기 쉬워지고, 관리도 편해짐)
# 2. 튜플에 저장된 내부 값에 접근하기 위해 위치 기반 정보로 접근하는 것은 깨지기 쉬운 코드다. (튜플에는 언제든 새로운 요구 사항으로 값이 추가될 수 있음. 특정 부분만 사용하기 위해 더 많은 무시 코드인 _, _를 추가해야함.)
  # 또한 튜플에서 값을 계속 추가하는 것은 그 자체로 '2중 딕셔너리'처럼 '튜플의 내포'가 늘어나는 것으로 볼 수 있음.
  # 따라서 튜플을 위치 기반으로 접근하는 것, 튜플에 계속 값을 추가하는 코드가 있다면 클래스로 변경하자.


from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Grade:
    score: int
    weight: float


class Subject:

    def __init__(self):
        self._grades = []

    def report_grade(self, grade):
        self._grades.append(grade)

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight

        return total / total_weight


class Student:
    subject_list: defaultdict[Subject]

    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


book = Gradebook()
albert = book.get_student('아인슈타인')
math = albert.get_subject('수학')
math.report_grade(Grade(75, 0.05))
math.report_grade(Grade(80, 0.05))
math.report_grade(Grade(100, 0.05))

print(albert.average_grade())



