class s:
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2
    def __add__(self, other):
        self.b1=self.a1+other.a1
        self.b2=self.a2+other.a2
        print (self.b1,self.b2)
s1 = s(55,55)
s2 = s(45,55)
s3 = s1+s2
print(s1.a1)