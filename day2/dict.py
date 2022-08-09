# 字典
phone = {
  "name": "我的手机",
  "price": 5000,
}

# 获取值
# price = phone["price"]

# get也可以获取值

# price = phone.get("price")

# 值的更改
phone["price"] = 122

# for in 遍历键名
for i in phone:
  print(phone.get(i))

# values() 可以返回字典的值
# list
for x in phone.values():
  print(x)

# 是否具有某个健 in
isKey = "name" in  phone
# print(isKey)
if isKey:
  print("具有name这个键")

# 有多少键对 len()

# 添加键对
phone["version"] = "iphone13"
print(phone)

# 删除键 pop() 方法删除具有指定键名的项

# popitem() 方法删除最后插入的项目（在 3.7 之前的版本中，删除随机项目）：

# del删除关键字的键名的项目
del phone["price"]
print(phone)

# del 完全删除字典
del phone

# clear() 清空字典

# copy() 复制字典

# 制作副本的另一种方法是使用内建方法 dict()

# 字典嵌套
child1 = {
  "name" : "Phoebe Adele",
  "year" : 2002
}
child2 = {
  "name" : "Jennifer Katharine",
  "year" : 1996
}
child3 = {
  "name" : "Rory John",
  "year" : 1999
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# dict() 构造函数
# clear()	删除字典中的所有元素
# copy()	返回字典的副本
# fromkeys()	返回拥有指定键和值的字典
# get()	返回指定键的值
# items()	返回包含每个键值对的元组的列表
# keys()	返回包含字典键的列表
# pop()	删除拥有指定键的元素
# popitem()	删除最后插入的键值对
# setdefault()	返回指定键的值。如果该键不存在，则插入具有指定值的键。
# update()	使用指定的键值对字典进行更新
# values()	返回字典中所有值的列表