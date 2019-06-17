#

"""
 三大结构
 - 顺序
 - 分支
  - 分支的基本逻辑
    - if 条件表达式：
        语句1
        语句2
        ...
        语句n
  - 条件各地怕啊就是计算结果必须为布尔值的表达式
  - 表达式后面的冒号不能少
  - 注意if后面的出现的语句，如果属于if诗句块则必须同一个锁等级
  - 条件各党派想法就送True执行if后面的缩进的语句块
 - 循环
  - 重复执行某些固定动作或者处理基本固定的事物
  - 分类
    - for循环
    - while 循环
"""

age = 18
if age < 19:
  print("年轻")
print("老了")

"""
双向分支
  - if...else...语句
      if 条件表达式：
          语句1
          ...
      else:
          语句1
          ...
  - 双向分支有两个分支，当程序执行到if...else..语句时，一定会执行if或else中的一个
  - 缩进问题,if和else一个层级，其余语句一个层级
"""

gender = input("请输入性别：")
print("你输入的性别是：{0}".format(gender))

if gender == "man":
  print("男人")
else:
  print("女人")


"""
多路分支
- 很多分支的情况，简称多路分支
    if 条件表达式：
        语句1
        ...
    elif 条件表达式：
        语句1
        ...
    elif 条件表达式：
        语句1
        ...
    elif 条件表达式：
        语句1
        ...
    ...
    else:
        语句1
        ...
- elif 可以有很w多
- else 可以没有
- 多路分支只会选一个执行    
"""

"""
if语句其他：
- if语句可以嵌套使用，但不推荐
- python 没有 switch-case语句
"""

"""
- for循环
  for 变量 in 序列：
      语句1
      ...
- 列表就是一列数字或者其它值，一般用中括号表示
  如：['1', '2', 'list']
"""
# range() 函数用法，含左不含有
for i in range(1, 10):
  print(i)


"""
for-else语句
- 当forr循环结束时，会执行else语句
- else语句是可靠语句
"""
for name in ['zhangsan', 'lisi', 'wjp']:
  print(name)
  if name == 'lisi':
    print("{0}".format(name))
  else:
    print("约不同学")
else:
  print("不在同学列表")


"""
for循环之break, continue, pass
  - break: 无条件结束整个循环
  - continue: 无条结束本次循环，重新进入下一轮循环
  - pass： 表示路过
python中，如果循环变量不重要，可以用下划线（_）代替
"""
for _ in range(1,2):
  print("不重要变量测试")

for i in range(1,5):
  if i == 4:
    print("find it")
    break
  else:
    print(i)

# 找偶数 1
for i in range(1,5):
  if i % 2 == 0:
    print("0} 是偶数".format(i))

# 找偶数 2
for i in range(1,5):
  if i % 2 == 1:
    continue
  print("0} 是偶数".format(i))

# pass 列子，一般用于占位
for i in range(2):
  pass
