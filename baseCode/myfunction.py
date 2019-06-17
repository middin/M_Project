#

"""
函数
- 代码的一种组织形式
- 一个函数一般完成一项功能
- 函数使用
  - 函数需要先定义
  - 使用函数，俗称调用
    - 定义一个函数
    - 只要y定义的话不会执行
      - 关键字 def
      - 函数名，自己定义，起名要有命名规则
"""

def func():
  print("这是一个函数")


"""
函数的参数和返回值
- 参数： 负责给函数货运站一些必要的数据或者信息
  - 参数只是一个符号，wager是调用时的某一个数据
    - 形参（形式参数）：在函数定义时没有具体值，只是一个点位符号
    - 实参（实际参数）：y在调用函数时输入的值
- 返回值： 函数的执行结果
  - 使用 return 关键字
  - 如果没有 return, 默认返回一个none
  - 执行了return,表示函数结束了
"""
def hello(person):
  print("{0}, 你好".format(person))

# return 语句的使用
def hello1(person):
  print("{0}, 你好".format(person))
  return ("成功获取{0}".format(person))

rst = hello1("test")
print(rst)

# 九九乘法表
def printline(row):
    for col in range(1, row+1):
      print("{0}*{1}={2}".format(col, row, row*col), end=' ')
    print()

def chengfabi():
  for row in range(1,10):
    printline(row)

"""
参数分类
  - 普通参数
    - 定义时直接定义变量名
    - 调用时直接把变量值放入指定位置
        def 函数名（参数1, 参数3, ...):
          语句块
        #调用
        函数名(value1, value3, ...)
  - 默认参数
    - 形参带有默认值
    - 调用时，如果没有对应形参赋值，则使用默认值
        def func_name(p1 = v1, p2 = v2, ...):
          语句块
        #调用 1
        fun_name()

        #调用2
        fun_name(10,20)

  - 关键字参数
    - 语法
        def func(p1=v1, p2=vv2,...):
          func_body
        # 调用
        func(p1=value1, p2=value,...)
    - 比较麻烦，但也有好处：
      - 不容易混淆，一般实参和形参只是按照位置一一对应都可，容易出错
      - 使用关键字参数，可以不考虑参数位置
  - 收集参数
    - 把没有位置，不能和定义时的参数位置相存放易燃参数，放入一个特定的数据结构中
    - 语法
        def func(*args):
          func body
          按照list使用方式访问args得到传入的d参数

        #调用
        func(p1, p2, p3...)
    - 参数名args不是必须这么写，但是推荐直接用args，约定
    - 参数名args前需要由星号
    - 收集参数可以和其他参数共存

"""
# 默认参数
def reg(name, age, gender="male"):
  print("{0}, 年龄：{1}，性别：{2}".format(name, age, gender))
  if gender == 'male':
    print("he is good student")
  else:
    print('she is good student')

reg("jhon", 21)
reg("lily", 22, "female")

# 关键字参数
def stu(name, age, addr):
  print("{0} is {1}, 住址：{2}".format(name, age, addr))

n = "jingjing"
a = 18
addr = "我家"
stu(n, a, addr) # 此处可能会出现  stu(a, n, addr)   调用顺序错

def stu_key(name="no name", age=0, addr="no addr"):
  print("{0} is {1}, 住址：{2}".format(name, age, addr))
stu_key(name=n, age=a, addr=addr)
stu_key(age=a, name=n, addr=addr)


#收集参数
def stud(*args):
  print(type(args))
  print(len(args))
  if len(args) == 5:
    print(args[0], args[1], args[2], args[3], args[4], sep="---", end="\n")
  for item in args:
    print(item, sep=",", end="")
  print()

stud("lily", 18, "北京大通州区", "jhon", "single")
stud("lucy", 18, "北京大通州区")

"""
收集参数之关键字收集参数
- 把关键字参数按字典式存入收集参数
- 语法
      def func(**args):
          func_body
      
      #调用
      func(p1=v1, p2=v2, ...)
- kwargs 一般约定俗成
- 调用时，把多余的关键字参数放kwargs
- 访问kwargs要按字典格式访问
"""

def studn(**kwargs):
  print(type(kwargs))
  for k,v in kwargs.items():
    print(k, "...", v)

studn(name="lily", age=14, addr="北京")
print("*" * 50)
studn(name="lucy")


"""
收集参数混合调用的顺序问题
- 收集参数，关键字参数，普通参数可以混合使用
- 使用规则：普通参数和关键参数优先
- 定义时一般找普通参数，关键字参数，收集参数tuple,以参数dict
"""
#收集参数混合调用实例
def studen(name, age, *args, hobby="没有", **kwargs):
  print("我叫 {0} , 今天 {1} 了".format(name, age))
  if hobby == "没有":
    print("没有爱好")
  else:
    print("爱好是：{0}".format(hobby))

  print("*" * 20)

  for i in args:
    print(i)
  print("*"*30)

  for k,v in kwargs.items():
    print(k, "...", v)

name = "liu"
age = 18
studen(name, age)

studen(name, age, hobby="游泳")

studen(name, age, "lily", hobby="游泳", hobby2="cooking", hobby3="chatting")

"""
收集参数的解包问题
- 把参数放入list或者字典中，直接把list/dict中的值放入收集参数中
- 语言：参考实例
"""
def stu(*args):
  print("哈哈")
  for i in args:
    print(i)
stu("liu", "niu", 13, 100)

l = list()
l.append("liuying")
l.append(20)
l.append(230)
stu(l) #此时  args = ([['liuying', 20, 230])

#此时调用解包符号
stu(*l)

"""
同理，dict类型收集参数一样可以解包， 但是
- 对dict类型进行解包
- 需要两个星号进行解包
"""

"""
返回值
- 函数和过程的区别
  - 有无返回值
- 需要用return显示返回内容
- 如果没有，则默认rclk None
- 推荐写法，无论有无返回值， 最后都要以return 结束
"""
def func_1():
  print("aaaa")
  return 1

def func_2():
  print("bbbb")

"""
函数文档
- 函数的文档的作用是对当前函数提供使用书的人参考信息
- 文档的写法
  - 在函数内部开始的第一行使用三字符r串定义符
  - 一般具有特定格式
  - 参考实例
- 文档查看
  - 使用help函数，如 help(func)
  - 使用doc
"""
def student(name, age, *args):
  '''
  这是文档的文字内容
  ：param name: 姓名
  : param age: 年龄
  : return: None
  '''
  print("this is hanshu student")

help(student)
print("*"*20)
print(student.__doc__) # student.__doc__  指令窗口可用

