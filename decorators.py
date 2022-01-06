def div(a,b):
    print(a/b)
def div1(func):
    def inn(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inn
div = div1(div)
div(2,4)