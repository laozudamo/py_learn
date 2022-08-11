# oy 模块
import mod1


# 注释：如果使用模块中的函数时，请使用以下语法：
# module_name.function_name

mod1.hello()

# 模块重新命名 用 as

# 内建模块
import platform


# 有一个内置函数可以列出模块中的所有函数名（或变量名）。dir() 函数：
# dir() 函数可用于所有模块，也可用于您自己创建的模块

# print(dir(platform))


# 您可以使用 from 关键字选择仅从模块导入部件

# from mymodule import person1
# 从哪个模块导入某一个部分