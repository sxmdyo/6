def maxTwo(a,b):
    if a>b:
        print(a)
    else:
        print(b)

def maxThree(x,y,z):
    if x>y:
        maxTwo(x,z)
    else:
        maxTwo(y,z)

maxTwo(3,4)
maxThree(1,2,3)

x=3,4,5,6
y=[3,4,5,6,]
print(x[1])
print(y[1])
a=[1,2,3,4,5,6,7,8]
a.append(2) #列表a最后添加元素2
print(a)

a.insert(2,100)#插入列表a里索引为2的位置，100这个值
