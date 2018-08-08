class math:
    def __init__(self,a):
        self.a=a
        self.b=10
    def add(self):
        print(self.a+self.b)
    def jian(self):
        print(self.a-self.b)

test1=math(3)
test2=math(4)
test1.add()
test2.jian()