class top10:
    def __init__(self):
        self.num =1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            vals=self.num
            self.num+=1
            return vals
        else:
            raise StopIteration
values = top10()
for i in values:
    print(i)
