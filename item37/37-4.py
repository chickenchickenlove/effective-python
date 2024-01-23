# 학생 이름 - 과목 - (점수, 가중치)로 관리 중임.
# 리프노드부터 리팩토링 하자

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
        for subject in self._subjects:
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



