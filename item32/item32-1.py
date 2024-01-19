
# 리스트 컴프리헨션으로 했을 때는 문제가 있을 수 있음.
# my_file.txt로 읽은 파일의 전체 라인 수가 수십조라면? 메모리에 다 넣을 수 없음... 문제임.
value = [len(x) for x in open('my_file.txt')]
print(value)