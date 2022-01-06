n=int(input("enter a number for factorial:"))
def fact(n):
    a=1
    for i in range (1,n+1):
        a*=i
    print(a)
fact(n)