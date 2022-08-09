
x = 'jack'

def testFun():
    x = ' dan'
    print (x + 'hello')

testFun()

print("Python is " + x)

# global 关键字
def globalFun():
  global jack
  jack = "hello jack"
  print (jack)

globalFun()

print("py " + jack)

# 函数内部改变外部的值

a = 'a 的初始值'

def changeAval():
  global a
  a = 'a 的初始值改变了'

changeAval()

print("py " + a)

# str
a = 'this is a str'
print(type(a))

# int
b = 3
print(type(b))

# float
c = 3.12
print(type(c))

# complex
z = 3j
print(type(z))

# list
d = [1, 2, 3, 4, 5, 6, 7]
print(type(d))

# tuple
e= ('12', '12', '12')

# dict
f = {a: 12, b: 34}

# 设定特定的数据类型使用构造函数
g = str('hello javk')

k = list(("apple", "banana", "cherry"))
