def sort_priority(values, group):
    found = False
    def helper(x):
        if x in group:
            # helper 안의 found는 자유변수가 아님. 즉, 외부의 found랑 무관함.
            found = True
            return 0,x
        return 1,x
    values.sort(key=helper)
    return found

n = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
print(sort_priority(n, group))





