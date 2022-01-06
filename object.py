class computer:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def config(self):
        print('he is',self.name,self.age)
c1=computer('sgv',22)
c2=computer('sg',22)
c1.config()
c2.config()
