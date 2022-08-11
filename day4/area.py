# python 作用域
# 变量仅在创建区域内可用。这称为作用域

# 作用域分为 全局作用域 和 函数作用域

from re import X


x = 'hello world'

# x这个时候是全局作用域


def changeval():
    global x
    x = "dany"
    # print(x)


changeval()
print(x)

# 如果在函数内部将会视为另外的变量 要想改变全局变量的值 请加上global

