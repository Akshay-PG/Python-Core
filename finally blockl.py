try:
    a=20
    b=0
    print(a/b)
except ZeroDivisionError:
    print("enter non zero value")
#any code written under finally block going to execute no matter what
finally:
    print('executed no matter what')