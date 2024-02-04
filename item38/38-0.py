

my_list = ['a', 'aa', '123', '1', '124123']
my_list.sort(key=len)
print(my_list)

def hello(my_dict):
    state = 0
    def real_func():
        nonlocal state
        state +=1

    for k,v in my_dict.items():
        real_func()
        print(k, v)
