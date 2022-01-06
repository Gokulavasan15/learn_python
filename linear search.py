a = [1,2,3,4,5,6,7,8,9]
n = int(input('enter a number to search:'))
def linsearch (list,n):
    for i in range(len(list)):
        if list[i]==n:
            print('found at index of',i)
            break
    else:
        print('not found')
linsearch(a,n)