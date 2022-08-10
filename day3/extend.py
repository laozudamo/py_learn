# 父类是继承的类，也称为基类。

# 子类是从另一个类继承的类，也称为派生类

class Person:
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def printname(self):
        print(self.first_name + " " + self.last_name)


p1 = Person("wang", "jack")

# p1.printname()


# class Student(Person):
#     pass

# s1 = Student("wang", "dan")

# s1.printname()

# 添加 __init__() 函数
# 到目前为止，我们已经创建了一个子类，它继承了父类的属性和方法。

# 我们想要把 __init__() 函数添加到子类（而不是 pass 关键字）。

# 注释：每次使用类创建新对象时，都会自动调用 __init__() 函数。

# 当您添加 __init__() 函数时，子类将不再继承父的 __init__() 函数。


# 注释：子的 __init__() 函数会覆盖对父的 __init__() 函数的继承
class Student(Person):
    def __init__(self, fname, lname, phone = None):
        # super().__init__(fname, lname)

        # 或者

        Person.__init__(self, fname, lname)
        self.fname = fname
        self.lname = lname
        self.phone = phone

    def getname(self):
        print(self.fname + " " + self.lname)


s2 = Student("wang", "lucy", 13258229689)

s2.getname()
s2.printname()
v = s2.phone
print(v)

# 在子类里面添加 __init__() 函数后如需保持父的 __init__() 函数的继承，请添加对父的 __init__() 函数的调用：

# 使用 super() 函数
# Python 还有一个 super() 函数，它会使子类从其父继承所有方法和属性：
# 通过使用 super() 函数，您不必使用父元素的名称，它将自动从其父元素继承方法和属性。

# 可以在子类里面添加新的属性和方法

# 提示：如果您在子类中添加一个与父类中的函数同名的方法，则将覆盖父方法的继承。
