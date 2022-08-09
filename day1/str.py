# 所有字符串方法都返回新值。它们不会更改原始字符串。

# 多行字符串
a = """asdas
  sasdasdsasdasdasd"""

b = '''121212
1212
1212'''

print(a, b)

c = "HelloWorld!"
print(c[2])

""" 
裁切
您可以使用裁切语法返回一定范围的字符。
指定开始索引和结束索引，以冒号分隔，以返回字符串的一部分
"""

lucy = 'lucy hahha'
print(lucy[0:2])

# 负号从末尾开始计数
# str[-3, -1]

# len() 函数返回字符串的长度：
# len(str)

# strip() 方法删除开头和结尾的空白字符
# a.strip()

# lower()方法返回小写; upper()方法返回大写
# a.lower() a.upper()

# replace()方法进行替换

# split() 方法在找到分隔符的实例时将字符串拆分为子字符串：

# 检查字符串 in 或者 not in
# txt_str = 'hello world'

# v = 'll' in txt_str

# print(v)

# 字符串级联（串联） + 号
# 添加空格  "121" + " " + "sad"
# 字符串和数字不能直接用 + 连接

# format 方法组合字符串和数字
# format() 方法接受传递的参数，格式化它们，并将它们放在占位符 {} 所在的字符串中：
# age = 63 
# txt = "My name is Bill, and I am {}"
# print(txt.format(age))
# 您可以使用索引号 {0} 来确保参数被放在正确的占位符中：
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# jack = 'jack'
# hello = jack.capitalize()
# print(hello)
