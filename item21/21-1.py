
# helper는 클로저가 됨.
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return 0,x
        return 1,x
    values.sort(key=helper)

n = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
sort_priority(n, group)
print(n)





