
def rangeTime(time):
  for i in range(time):
    print(i)
  else:
    print('done')

# rangeTime(10)

# for 循环中的 else 关键字指定循环结束时要执行的代码块：

# 嵌套循环

list  = [
  {
    'id': 1,
    'name': 'A',
  },
  {
    'id': 2,
    'name': 'B',
  }
]

for i in list:
  for j in i:
    print(i[j])

# pass 语句 避免空if的错误
