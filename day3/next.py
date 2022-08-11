# Python 迭代器

# 在 Python 中，迭代器是实现迭代器协议的对象，它包含方法 __iter__() 和 __next__()

# 所有这些对象都有用于获取迭代器的 iter() 方法：

mystr = "banana"
myit = iter(mystr)
print(next(myit))

# for 循环实际上创建了一个迭代器对象，并为每个循环执行 next() 方法。
