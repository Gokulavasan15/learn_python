from pandas import *
a = {'name': ['sg','gv','nj','sgv'],'age':[1,2,3,4]}
print(a)
f = DataFrame(a)
print(f)
b= f['age']
print(b)