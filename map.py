my_list =[1,2,3,4,5,6,7]

def add(x):
    return x+2

s = list(map(add,my_list))
print(s)