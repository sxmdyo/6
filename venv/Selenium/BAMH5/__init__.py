print("方法一：")
for i in range(1,11):
    print(i)

print("方法二：")
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i)

sum = 0
i = 1
while i<101:
    sum +=1
    i =i+1
print(sum)


x = 4
y = 4
z = 10

if x<y:
    print("x比y小")
elif x>y:
    print("x>y")
else:
    print("x=y")


if x<z:
    print("x<z")
if y<z:
    print("y<z")

def example():
    print("这是一个函数的例子")

example()



def maxTwo(a,b,c):
    if a>b:
        print(a,c)
    else:
        print(b,c)

maxTwo(2,2,3)

x=6
def printFuc():
        y=8
        w=9
        print(y+z)
        print(x)


printFuc()
print(x)

#读取csv文件，以列表的形式展示
import csv
try:
    with open(r'/Applications/test1.csv') as csvFile:
        readCSV=csv.reader(csvFile,delimiter=',')
        for row in readCSV:
            print(row)
except Exception as e:
    print(e)
    print("请确认csv的路径是否正确")
#多行打印
print('''
第一行内容
第二行内容
第三行内容
。。。。
==========================
|                       |
|                       |
|                       |
|       Welcome   切切      |
|                       |
|                       |
|                       |
==========================
''')

#字典
tem={'name1':['songxueming','23'],'name2':['sunliwei','26'],'name3':['hanjialiang','22']}

print(tem['name3'])
print(tem['name1'][1])
