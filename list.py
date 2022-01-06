lst=[]
n=int(input("enter the number of names"))
for i in range (n):
    x=str(input("enter the name"))
    lst.append(x)
print(lst)
c=0
for j in lst:
    if len(j)>2:
        c+=1
print(c)
