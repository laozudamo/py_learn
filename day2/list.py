from itertools import count


testList = [1, 2, 3, 4, 10]
# for item in testList:
#     print(item)


def checkList():
    if(2) in testList:
        print("yes")


checkList()


def hello():
    print("Hello!")


# hello()


testList2 = ['apple', 'blanan', 'orange']

# 末尾添加
# testList2.append('black')

# 插入
# testList2.insert(1, 'black')

# 切割数组
# val = testList2[1: 3]

# 删除指定项目
# testList2.remove('apple')

# pop() 方法删除指定的索引
# testList2.pop()

# print(testList2)

# print(testList2, val)

# del删除指定的索引
# del testList2[0]

# del 关键字也能完整地删除列表：
# del testList2

# clear() 方法清空列表：
# testList2.clear()

# copy() 方法来复制列表
# myList = testList2.copy()
# print(myList)

# list()。

# 合并两个列表：
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# extend list1 to include the same number of
list1 = ["a", "b", "c"]
list2 = [1, 1, 3]

list1.extend(list2)
print(list1)

v = list1.count(1)
print(v)
# list() 构造函数
# 也可以使用 list() 构造函数创建一个新列表。

# 列表
list3 = list((1, 2, 3))
print(list3)
