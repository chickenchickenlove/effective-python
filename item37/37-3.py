# 학생 이름 - 과목 - (점수, 가중치)로 관리 중임.
# 이제 새로운 요구사항이 추가되었음. 점수 + 가중치를 이용해 전체 점수를 내도록 함.
# 1. 이 요구사항이 추가되면서 average_grade쪽 코드는 엄청나게 복잡해짐.
# 2. 클라이언트 코드도 파라메터가 늘어나면서, 이해하기 어려워짐.
# 딕셔너리가 2단계 내포되었으나, 튜플(점수, 가중치)이 2단계로 내포되면서 3단계 정도로 내포됨.
# 이런 식으로 계속 내포가 발생하는 코드는 다음 문제점이 있다.
# 1. 클라이언트가 사용하기 어려움.
# 2. 코드 유지보수가 어려움. (무슨 데이터가 오는지 정확히 알 수 없음)
# 결론적으로 내포 단계가 두 단계 이상이 되면, 딕셔너리 / 리스트 / 튜플 계층을 더 이상 추가하지 않아야 함.

from collections import defaultdict


class WeightedGradebook:
    def __init__(self):
        self._grades = {} # 외부 dict

    def add_student(self, name):
        self._grades[name] = defaultdict(list) # 내부 dict

    # name: 학생 이름 / subject : 과목 / grade : 점수
    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight)) # 이제 weight를 튜플로 같이 추가함.

    def average_grade(self, name):
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0

            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight

            score_sum += subject_avg / total_weight
            score_count += 1

        return score_sum / score_count


book = WeightedGradebook()
book.add_student('아이작 뉴턴')
book.report_grade('아이작 뉴턴', '수학', 90, 0.05)
book.report_grade('아이작 뉴턴', '체육', 95, 0.15)
book.report_grade('아이작 뉴턴', '물리', 85, 0.80)

print(book.average_grade('아이작 뉴턴'))



