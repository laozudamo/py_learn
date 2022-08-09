# 元组一旦创建，您就无法向其添加项目。元组是不可改变的。
tupleList = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupleList[0])
print(tupleList[-1])
print(tupleList[1: 2])

y = list(tupleList)

# def getAllItem():
#   for i in tupleList:
#     print(i)

# getAllItem()

v = 1 in tupleList
print(v)

l = len(tupleList)
print(l)

# 元组是不可更改的，因此您无法从中删除项目，但您可以完全删除元组
del tupleList

# 合并两个元组

# tuple() 构造函数 用来进行构造元祖
# count()
# index()