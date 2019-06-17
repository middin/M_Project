#
'''
Python 语言的高级特性
- 函数式编程(FunctionalProgramming)
  - 基于lambda演算的一种编程方式
    - 程序中只有函数
    - 函数可以作为参数，同样可以作为返回值
    - 纯函数式编程语言： LISP，Haskell
  - Python函数式编程只是借鉴函数式编程的一些特点，可以理解成一半函数式一个Python
  - 需要讲述
    - 高阶函数
    - 返回函数
    - 匿名函数
    - 装饰器
    - 偏函数
- lambda 表达式
  - 函数： 最套种充复用代码
    - 存在问题：如果函数很小，很短，则会造成啰嗦
    - 如果函数被调用次数少，则会造成浪费
    - 对于阅读者来说，造成阅读流程的被迫中断
  - lambda 表达式(匿名函数)
    - 一个表达式，函数体相对简单
    - 不是一个代码块，仅仅是一个表达式
    - 可以有参数，有多个参数也可以，用逗号隔开
'''
# 小函数举例
def printA():
  print("AAAAAAAAAAAAA")

#printA()

# lambda表达式的用法
# 1. 以 lambda 开头
# 2. 紧跟一定的参数(如果有的话)
# 3. 参数后用冒号和表达式主题隔开
# 4. 只是一个表达式，所以没有return

# 计算一个数字的100倍数
# 因为是一个表达式，所以没有return
stm = lambda x: 100*x
print(stm(2))

stm2 = lambda x,y,z: x+y*10+z*100
print(stm2(2,3,4))


# 高阶函数
# - 把函数作为参数使用的函数，叫高阶函数
# 函数名称就是一个变量
a = printA
a()
# 以上代码得出结论
# - 函数名称是变量
# - a 和 printA 只是名称不一样而已
# - 既然函数名称是变量，则应该可以被当做参数传入另一个函数
# - 

# 高阶函数举例
# funA是普通函数，返回一个传入数字的100倍数字
def funA(n):
  return n*100

# 再写一个函数，把传入参数乘以300倍，利用高阶函数
def funB(n):
  # 最终是想返回300n
  return (funA(n)*3)

print(funB(9))
# 写一个高阶函数
def funC(n, f):
  # 假定函数把n扩大100倍
  return f(n)*3
print(funC(9, funA))
# 比较funC和funB，显示funC的写法要优于funB
# 
def funD(n):
  return n*10
# 需要把n 放大30化妆品，此时funB则无法实现
print(funC(7, funD))

'''
系统高阶函数 - map
- 愿意就是映射，即把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表或者集合
- map 函数是系统提供的具有映射功能的函数，返回值是一个迭代对象
'''
# map 实例
# 有一个列表，想对列表里面的每一个元素f乘以10，并得到新列表
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
  l2.append(i*10)
print(l2)
# 利用map实现
def mulTen(n):
  return n*10

l3 = map(mulTen, l1)
# map 类型是一个可迭代的结构，所以可以使用for遍历
for i in l3:
  print(i)
print(l3)
# 以下列表生成式得到的结果为空
l4 = [i for i in l3]
print(l4)

'''
reduce
- 原意是归并，缩减
- 把一个可迭代对象最后归并成一个结果
- 对于函数参数由函数要求： 必须由两个参数，必须由返回结果
- reduce([1,2,3,4,5])  == f(f(f(f(1,2),3),4),5)
- reduce 需要导入functools包
'''
from functools import reduce

# 定义一个操作函数
# 假如操作函数只是相加
def myAdd(x,y):
  return x+y
# 对于列表 [1,2,3,4,5,6] 执行myAdd的reduce操作
rst = reduce(myAdd, [1,2,3,4,5,6])
print(rst)

''' 
filter 函数
- 过滤函数：对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回
- 跟map相比较：
  - 相同：都对列表的每一个元素逐一操作
  - 不同：
    - map 会生成一个跟原来数据相对应的新队列
    - filter不一定，只要符合条件的才会进入新的数据集合
  - filter函数写法：
    - 利用给g定函数进行判断
    - 返回值一定是个布尔值
    - 调用格式： 
      - filter(f, data), f是过滤函数，data是数据
'''
# filter 案例
# 对于一个列表，进行过滤，偶数组成一个新列表
# 需要定义过滤函数
# 过滤函数要求有输入，返回布尔值
def isEven(a):
  return a%2==0

l = [i for i in range(10)]
rst = filter(isEven, l)
# 返回的filterw内容是一个可迭代对象
print(type(rst))
print(rst)
print([ i for i in rst])

'''
高阶函数-排序 sorted
- 把一个序列按照给定算法进行排序
- key: 在排序 对每一个元素进行key函数运算，可以理解成按照key函数排序
- Python2.x 和 Python3.x 相关世贸大厦
'''
# 排序 案例 1
a = [23,1231,15,1324,5656,4]
a1 = sorted(a)
print(a1)

# 排序 案例 2
a = [-21, 234, 11, -111, 2, -88]
# 按照绝对值进行排序
# 即按照绝对值的倒叙排列
al = sorted(a, key=abs, reverse=True)
print(al)

# 排序 案例 3
astr = ['dana', 'Danaa', 'wangxiaojing', 'jingjing','haha']
str1 = sorted(astr)
print(str1)
str2 = sorted(astr, key=str.lower)
print(str2)

'''
返回函数
- 函数可以返回具体的值
- 也可以返回一个函数作为结果
'''
# 定义一个普通函数
def myF(a):
  print("In myF")
  return None
a = myF(0)
print(a)

# 把函数作为一个返回值返回， 被返回的函数在函数体内定义
def myF2():
  def myF3():
    print("In myF3")
    return 3
  return myF3
# 使用上面定义
# 调用myF2，返回一个函数myF3,赋值给F3
f3 = myF2()
print(f3)
print(f3())

# 复杂一点的c返回函数的例子
# args: 参数列表
def myF4(*args):
  def myF5():
    rst = 0
    for n in args:
      rst += n
    return rst
  return myF5

f5 = myF4(1,2,3,4,5,6,7,8,9,0)
# f5的调用方式
print(f5())

'''
闭包（closure)
- 当一个函数在内部定义函数，并且内部函数应用外部函数的参数或者局部变量，当内部函数被当做返回值时，相关参数和变量保存在返回的函数中，这种结构叫闭包
- 上面定义的myF4是一个标准闭包结构
'''
# 闭包常见坑
def count():
  fs = []
  for i in range(1,4):
    # f是一个闭包结构
    def f():
      return i*i
    fs.append(f)
  return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

# 出现的问题
# 造成上述状况的原因是，返回函数引用了变量i,i并非立即执行，南昌是等到三个函数都返回时才统一y使用，此时i已经变成了3，最终调用时，都返回的是 3*3
# 此问题描述成：返回闭包时，返回函数不能引用任何循环变量
# 解决方案：再创建一个函数，用该函数的参数绑定循环变量的当前值，无论该循环变量以后如何发言为，已经绑定的函数参数值不再改变
# 修改以上函数
def count1():
  def f(j):
    # f是一个闭包结构
    def g():
      return j*j
    return g
  fs = []
  for i in range(1,4):
    fs.append(f(i))
  return fs

f1,f2,f3 = count1()
print(f1())
print(f2())
print(f3())
print("*"*50)

# 装饰器
def hello():
  print("hello")
hello()
f = hello
f()
# f 和 hello是一个函数
print(id(f))
print(id(hello))
print(f.__name__)
print(hello.__name__)

# 对hello功能进行扩展，每次打印hello之前打印当前系统时间
# 而实现这个功能又不能改动现有代码
# ==> 使用装饰器
# 装饰器
# - 在不改动函数代码的基础上无限制扩展函数功能的一种机制，配制上讲，装饰器是一个返回函数的高阶函数
# - 装饰器的使用: 使用@语法，即在每次要扩展到函数定义前使用@+函数名
# 
import time

# 高阶函数，以函数作为参数
def printTime(f):
  def wrapper(*args, **kwargs):
    print("Time: ", time.ctime())
    return f(*args, **kwargs)
  return wrapper
# 上面定义了装饰器，使用时需要用@，此符号是python的语法糖
@printTime
def hello():
  print("hello world")

hello()
# 装饰器的好处是，一点定义，则可以装饰任意函数
# 一旦被装饰，刚把装饰器的功能直接添加到定义函数的功能上
@printTime
def hello2():
  print("111111111111111")
  print("222222222222222")
hello2()

# 上面对函数的装饰使用了系统定义的语法
# 下面开始手动执行下装饰器
# 先定y义函数
def hello3():
  print("手动执行")

hello3()
hello3 = printTime(hello3)
hello3()
# 下面调用会出现两次时间，为啥
f = printTime(hello3)
f()

# 把字符串转化成十进制数字
int('12345')
# 想把字符串 12345 转化成八进制整数
print(int('12345', base=8))

# 新建一个函数，此函数是默认输入的字符串是16进制数字
# 把此字符串返回十进制数字
def int16(x, base=16):
  return int(x, base)
print(int16("12345"))

# 偏函数
# - 参数固定的函数，相当于一个由特定参数的函数体
# - functools.partial的作用是，把一个函数某些函数固定，返回一个新函数
import functools
# 实现上面int16的功能
int16 = functools.partial(int, base=16)
print(int16("12345"))