a = [1,2,3,4,5,6,7,8,9]
n = int(input('enter a number to search:'))
def binsearch (list,n):
    l = 0
    u = len(a) - 1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            print('found at index',mid)
            break
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid+1
    else:
        print('not found')
binsearch(a, n)