def add(x):
    return(x+10)

def twice(y,z):
    return y(y(z))

print(twice(add,30))
