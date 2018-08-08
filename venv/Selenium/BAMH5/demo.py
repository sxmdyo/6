import time as t
timenow=t.localtime()
print(t.strftime('%Y-%m-%d %H:%M:%S',timenow))
class calculator():
    def add(x,y):
        addresult=x+y
        print(addresult)
    def sub(x,y):
        subresult = x - y
        print(subresult)
    def mul(x,y):
        mulresult = x * y
        print(mulresult)
    def div(x,y):
        divresult = x/y
        print(x/y)
calculator.add(2,3)
calculator.div(4,6)
calculator.mul(2,4)
calculator.div(3,1)