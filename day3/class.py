class MyClass:
    x = "hello my class"


p1 = MyClass()
print(p1.x)

# __init__() 函数


# 注释：每次使用类创建新对象时，都会自动调用 __init__() 函数。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
    def myFun(self):
      print("Hello my name is " + self.name)


p1 = Person('wang jack', 19)

print(p1.name)

# 提示：self 参数是对类的当前实例的引用，用于访问属于该类的变量
p1.myFun()

# 修改对象属性
p1.age = 200

# 删除对象属性
del p1.age

# 删除对象 del p1
del p1

# pass 语句
# 类定义不能为空，但是如果您处于某种原因写了无内容的类定义语句，请使用 pass 语句来避免错误。