from numpy import *

a = array([1,2,3,4])
a1 = array([1,2,3,4,])
a2 = array([])
for i in range(len(a)):
    x = a[i]+a1[i]
    a2 = append(a2,[x])
print(a2)
print(a)
print(a1)