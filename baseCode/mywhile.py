#

"""
while循环
- 一个循环语句
- 表示当某条件成立时，就循环
- 不知道具体循环次，但能确定循环的成立条件时就用while 循环
- while 语法：
    while 条件表达式：
        语句块
"""

#如果说年利率是6.7%，则多少年后会翻倍
benqian = 100000
year = 0
while benqian < 200000:
  benqian = benqian*(1+0.067)
  year += 1
  print("第 {0} 年拿了 {1} 块钱".format(year, benqian))
else:
  print("终于翻倍了，10多年")