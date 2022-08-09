# Python 集合
# 集合是无序和无索引的集合。在 Python 中，集合用花括号编写。

testSet = {1, 'apple', 'banana', 'orange'}

print(testSet)

# for in 遍历集合


def mapTestSet():
    for i in testSet:
        print(i)


# mapTestSet()


# 检查是否具有某元素

isApple = 'apple' in testSet

# 添加项目 add

testSet.add('hello')

# update 添加多个项 添加同样也是无序的
testSet.update(["orange", "mango", "grapes"])

# 获取长度 len()

# 删除项目remove
# 注释：如果要删除的项目不存在，则 remove() 将引发错误。
testSet.remove(1)
print(testSet)

# discard也可以用于set集合的删除 如果删除的项目不存在不会报错
testSet.discard("orange")
print(testSet)

# 使用pop也可以删除项目 但此方法将删除最后一项。请记住，set 是无序的，因此您不会知道被删除的是什么项目。
# pop()方法的返回值 是被删除的项目

delItem = testSet.pop()
print(delItem)

# clear方法清空集合
# del方法删除集合

# update方法将一个集合的所有元素插入到另一个集合中 只会取一次
# union方法返回两个集合中的所有项目 只会取一次
# union() 和 update() 都将排除任何重复项。

test2 = {1, 2, 3, 4}
test3 = {1, 2, 3, 5}
# test2.update(test3)
# test4 = test2.update(test3)
# print(test2)

# set方法的构造函数

# add()	向集合添加元素。
# clear()	删除集合中的所有元素。
# copy()	返回集合的副本。
# difference()	返回包含两个或更多集合之间差异的集合。
# difference_update()	删除此集合中也包含在另一个指定集合中的项目。
# discard()	删除指定项目。
# intersection()	返回为两个其他集合的交集的集合。
# intersection_update()	删除此集合中不存在于其他指定集合中的项目。
# isdisjoint()	返回两个集合是否有交集。
# issubset()	返回另一个集合是否包含此集合。
# issuperset()	返回此集合是否包含另一个集合。
# pop()	从集合中删除一个元素。
# remove()	删除指定元素。
# symmetric_difference()	返回具有两组集合的对称差集的集合。
# symmetric_difference_update()	插入此集合和另一个集合的对称差集。
# union()	返回包含集合并集的集合。
# update()	用此集合和其他集合的并集来更新集合。