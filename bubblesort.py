a=[9,6,4,6,3,2,8,7]
print(sorted(a))
def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
bubblesort(a)
print(a)