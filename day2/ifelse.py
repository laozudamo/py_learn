

def getBigger(num1, num2):
    if(num1 > num2):
        print("Bigger is num1")
    elif(num1 < num2):
        print("Bigger is num2")
    else:
        print("两个数相等喔")


getBigger(22, 22)


# 您也可以使用没有 elif 的 else

def newBigger(num1, num2):
  if(num1 > num2):
        print("Bigger is num1")

  else:
      print("Bigger is num2")

newBigger(10, 12)

# 简写

if 5 > 3: print("Bigger is 5")

a = 200
b = 200
# print("Bigger is a") if a > b else print("Bigger is b")

# 多个条件简写
print(a) if a > b else print("Bigger is b") if a < b else print("a === b")


# and 关键字是一个逻辑运算符，用于组合条件语句：

# Or 关键字也是逻辑运算符，用于组合条件语句：

# 您可以在 if 语句中包含 if 语句，这称为嵌套 if 语句。

# pass 语句
# if 语句不能为空，但是如果您处于某种原因写了无内容的 if 语句，请使用 pass 语句来避免错误。





