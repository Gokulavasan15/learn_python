n=int(input("enter a number,n="))
if n<1:
    print('input not valid')
else:
    def fib(n):
        a=0
        b=1
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range (2,n):
                c=a+b

                if c>n:
                    break
                else:
                    a=b
                    b=c
                    print(c)

            
    fib(n)
          
