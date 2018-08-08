class ClassA(object):
    string1 = "这是一个字符串"

    def instancefunc(self):
        print('这是一个实例方法')
        print(self)

    @classmethod
    def classfun(cls):
        print("这是一个类方法")
        print(cls)
    @staticmethod
    def staticfun():
        print("这是一个静态方法")
test = ClassA()#test是classA类的一个实例对象
test.instancefunc() #对象调用实例方法
test.classfun()#对象调用类方法
test.staticfun()#对象调用静态方法

print(test.string1)#对象调用
ClassA.instancefunc(test) #类调用实例方法需要带参数
ClassA.instancefunc(ClassA)

ClassA.classfun()#类调用类方法
ClassA.staticfun()#类调用静态方法