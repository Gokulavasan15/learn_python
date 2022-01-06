a=[9,8,7,6,5,4,3,2,1]
def selectionsort(list):
    for i in range(8):
        min = i
        for j in range(i,9):
            if a[j]<a[min]:
                min = j

        a[i],a[min]=a[min],a[i]


selectionsort(a)
print(a)