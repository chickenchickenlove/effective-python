# 학생 이름 - 과목 - 점수로 관리 중임.
# 1. 다단계 딕셔너리를 처리해야하기 때문에 클래스 코드 자체는 복잡해졌음.
# 2. 그러나 클라이언트쪽 코드는 여전히 사용하기 괜찮아보임.
# 따라서 딕셔너리가 2단계 내포되는 정도는 괜찮다.

from collections import defaultdict

class BySubjectGradebook:
    def __init__(self):
        self._grades = {} # 외부 dict

    def add_student(self, name):
        self._grades[name] = defaultdict(list) # 내부 dict

    # name: 학생 이름 / subject : 과목 / grade : 점수
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0,0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


book = BySubjectGradebook()
book.add_student('아이작 뉴턴')
book.report_grade('아이작 뉴턴', '수학', 90)
book.report_grade('아이작 뉴턴', '체육', 95)
book.report_grade('아이작 뉴턴', '물리', 85)

print(book.average_grade('아이작 뉴턴'))



