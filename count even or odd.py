lst=[]
n=int(input("enter len"))
for j in range(n):
    x=int(input("enter numbers"))
    lst.append(x)
print(lst)
def count(lst):
    c = 0
    d = 0
    for i in lst:
        if i%2==0:
            c+=1
        else:
            d+=1
    print("no of even",c)
    print("no of odd",d)
count(lst)
