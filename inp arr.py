from array import *
arr = array('i',[])
n = int(input("enter the length of the array"))
for i in range (n):
    x = int(input("enter the element of the array"))
    arr.append(x)
print(arr)
val = int(input("enter the value for search"))
k = 0
for a in arr:
    if val == a:
        print(k)
        break
    k+=1
    

