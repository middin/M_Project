#

"""
变量作用域
- 变量由作用范围限制
- 分类：按照作用域分类
  - 全局(global):在函数外部定义
  - 局部(local):在函数内部定义
-变量的作用范围
  - 全局变量：在整个全局范围都有效
    - 全局变量在局部可以使用，即函数内部可以方位函数外部定义的变量
  - 局部变量：在局部范围可以用
    - 局部变量在全局范围无法使用
-LEGB原则
  - L（Local): 局部作用域
  - E（Enclosing function locale) 外部嵌套函数作用域
  - G(Global module) 函数定义所在模块作用域
  - B(Buildin) python 内置魔抗作用域
"""
a1 = 100
def fun():
  print(a1)
  a2 = 98
  print("a2 = {0}".format(a2))

#print(a1)

"""
提升局部变量为全局变量
- 使用global
- 案例如下
"""
def fun():
  global b1
  b1 = 88
  print(b1)
  b2 = 99
  print(b2)

fun()
#print(b1)

"""
globals, locals函数 ---> 内建函数
- 可以通过globals和locals显示出局部变量和全局变量
- 参考以下案例
"""
a = 1
b = 2
def fun(c,d):
  e = 111
  print("locals={0}".format(locals()))
  print("globals={0}".format(globals()))

#fun(200,199)

"""
eval()函数
- 把一个字符串当成一个表达式执行，返回表达式执行后的结果
- 语法：
        eval(string_code, globalls=None, locals=None)
"""
x = 100
y = 200
z1 = x+y
z2 = eval("x+y") # z = x + y
print(z1)
print(z2)

"""
exec() 函数
- 跟eval功能类似，但是，不返回结果
- 语法：
        exec(string_code, globalls=None, locals=None)
"""
x = 100
y = 200
z1 = x+y
z2 = exec("print('x+y:', x+y)") # z = x + y
print(z1)
print(z2)

"""
递归函数
- 函数直接或者间接调用自身
- 优点： 简洁，理解容易
- 缺点： 对递归深度有限制，消耗资源大
- python 对递归深度有限制，超过限制报错
- 在写递归程序的时候，一定要注意结束条件
"""
# 递归调用深度限制代码
x = 9
def fun():
    global x
    x+=1
    print(x)
    #fun()

fun()

"""
斐波那契数列
- 一列数字
    第一个是1， 第二个也是1，从第三个开始，每一个数字的值等于前两个数字出现的值 的和
    数字公式为： f(1) = 1, f(2) = 1, f(n) = f(n-1) + f(n-2)
    例如： 1,1,2,3,5,8,13,....
"""
# n 表示第n个数字的斐波那契数列的值
def fib(n):
    if n == 1 or n == 2:
        return 1
    
    return fib(n-1)+fib(n-2)

num = fib(3)
print(num)


"""
内置数据结构（变量类型）
- list(列表)
- set
- dict
- tuple
"""
"""
- list(列表)
    - 一组由顺序的数据的组合
    - 创建列表
        - 空列表
- 访问
    - 使用下标操作（索引)
    - 列表的位置是从0开始
- 分片操作
    - 对列表进行任意一段的截取
    - l[:]
    - 例子：
        - ll[a:b:c]: a,b,c 为正，都为负时调转输出
            - a 为起始位置， 不包含当前下标值 
            - b 为终止位置， 包含当前下标值
            - c 为增长幅度
        - 超过下标，直接忽略
    - 从左向右截取
"""
l1 = []
# type 是内置函数，负责打印变量的类型
print(type(l1))
print(l1)

# 创建带的列表
l2 = [100]
print(type(l2))
print(l2)

# 下标访问列表
l = [2, 3, 4, 1, 8]
print(l[1:2])
print(l[-3:-1])

"""
分片操作是生成一个新的list
- 内置函数id, 负责显示一个变量或者数据的唯一确定编号
"""
# id函数实例
a = 100
b = 200
c = a
print(id(a))
print(id(b))
print(id(c))

# 通过id可以直接判断出分片是重新生成了一份数据还是使用的同一份数据
l = [3, 4, 56, 76, 32, 21, 43, 5]
ll = l[:]
lll = ll
# 如果两个id值一样，则青蛙分片产生的列表是使用的同一地址同一份数据
# 否则，则表明分片是重新生成了一份数据，即一个新列表，然后把数值拷贝到新q列表中
print(id(l))
print(id(ll))
print(id(lll))

# 通过id知道，ll和lll是同一份数据，验证代码如下
l[1] = 100
print(l)
print(ll)

ll[1]=100
print(ll)
print(lll)
