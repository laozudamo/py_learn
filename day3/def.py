# python 函数
# 函数是一种仅在调用时运行的代码块


def sayhi(name):
    print('hello' + name)


sayhi('lili')

# 同样也可以传默认参数


# 默认参数可以增加函数的健壮性
def sayhi(name="王杰克"):
    print('hello' + name)


sayhi()

# 同样也可以传数组

# 得到函数的返回值 用return


def getSum(num1, num2):
    if type(num1) is int and type(num2) is int:
        return num1 + num2


v = getSum(2, 3)
print(v)

# 任意参数
# 如果您不知道将传递给您的函数多少个参数，请在函数定义的参数名称前添加 *

# lambda 函数是一种小的匿名函数。