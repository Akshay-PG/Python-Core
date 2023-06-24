import numpy as np
d = np.array([1,2,3,4,5,6,7,8,9])
print(d)

#changing data type
s = np.array([1,2,3,4,5,6,7,8,9],dtype=np.float64)
print(s)

#accessing item
print(s[0])
print(d[6])
print(d[1:-1])
print(d[-1:-5])
print(d[-5:-1])

#changing value

s[2]=500
print(s)

# ARRAY CAN CONTAIN ONLY ONE DATA TYPE

#adding
print(s+d)

x=s+d
print(x)

#find minimum value
min_s = np.min(s)
print(min_s)

#find minimum value
max_s = np.max(s)
print(max_s)

#sort
sort_s = np.sort(s)
print(sort_s)

sort_s= np.array(sort_s,dtype=int)
print(sort_s)

#reverse order
s=np.flip(s)
print(s)

s=np.array(s,dtype=int)
print(s)

#mean
s_mean = np.mean(s)
print(s_mean)

#median
s_median=np.median(s)
print(s_median)

# STANDARD DEVIATION std : tells us how much the elements in an array deviates from MEAN
s_std = np.std(s)
print(s_std)





