b = 5
def scope():
    global b
    b = 6
    print("in func",b)
scope()
print("out fun",b)
a = 10
def scope1():
    a=15
    x=globals()['a']
    print("in func", a)
    globals()['a']=11
scope1()
print("out fun",a)
