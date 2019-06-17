#

class A():
  pass

class B(A):
  pass

class C(B,A):
  pass

# MRO 查找类的关系
print(A.__mro__)
print(B.__mro__)
print("*"*50)

'''
- 单继承和多继承
  - 单继承：每个类只能继承一个类
  - 多继承：每个类允许b继承多个类
- 单继承和多继承的优缺点
  - 单继承
      - 传承有序逻辑清晰语法简单隐患少
      - 功能不能无限扩展，只能在当前唯一的继承链中扩展
  - 多继承
      - 优点： 类的功能扩展方便
      - 缺点： 继承关系混乱
- 菱形继承/钻石继承
  - 多个子类继承于同一个父类，这些子类又被同一个类继承于是继承关系图开成一个菱形图形
  - 关于多继承的 MRO 
      - MRO 就是多继承中，用于保存继承顺序的一个列表
      - python 本身采用C3算法来多多继承的菱形继承进行计算的结果
      - MRO 列表的计算原则：
        - 子类永远在父类前面
        - 如果多个父类，则根据继承语法中括号内类的书写顺序存放
        - 如果多个类继承了同一个父类，孙子类中只会选取继承语法括号中第一个父类的父类
- 构造函数
  - 在对象进行实例化时，系统自动调用的一个函数叫构造函数，通常此函数用来实例化对象操作

- 多态
  - 多态就是同一个对象在不同的情况下有不同的状态出现
  - 多态不是语法，是种设计思想
  - 多态性，一种调用方式，不同的执行效果
  - 多态： 同一事物的多种形态，动物分为人类，狗类，猪类

- Mixin设计模式
  - 主要采用多继承的方式对类的功能进行扩展
  - 

- 使用多o继承语法来实现 Mixin
- 使用Mixin实现多继承时要非常小心
  - 首先必须表示某一单一功能，而不是某个物品
  - 职责必须单一，如果由多个功能，则写多个Mixin
  - Mixin不能依赖于子类的实现
  - 子类即使没有继承这个Mixin类， 也能工作，只是缺少了某个功能
- 优点
  - 使用mixin可以在不对类进行任何修改的情况下，扩充功能
  - 可以方便的组织和维护不同功能组件的划分
  - 可以根据需要任意调整功能类的组合
  - 可以避免创建很多新类，导致类的继承混乱

类相关函数
- issubclass： 检测一个类是否是一个类的子类
- isinstance:  检测一个对象是i否是一个类的实例
- hasattr: 检测一个对象是否有成员 xxx
- getattr: 获取
- setattr: 设置
- delattr: 删除
- dir: 

'''
# 多继承的例子
# 子类可以直接拥有父类的属性和方法，私有属性和方法除外
class Fish():
  def __init__(self, name):
    self.name = name
  
  def swim(self):
    print("I am swimming....")

class Bird():
  def __init__(self, name):
    self.name = name
  
  def fly(self):
    print("I am flying...")

class Person():
  def __init__(self, name):
    self.name = name
  
  def work(self):
    print("working.....")

# 单继承的例子
class Student(Person):
  def __init__(self, name):
    self.name = name

stu = Student("yueyue")
stu.work()

# 多继承
class SwimMan(Person, Fish):
  def __init__(self, name):
    self.name = name

class SuperMan(Person, Bird, Fish):
  def __init__(self, name):
    self.name = name

s = SuperMan("yy")
s.fly()
s.swim()
print("*"*50)

# 菱形继承问题
class A():
  pass

class B(A):
  pass

class C(A):
  pass

class D(B,C):
  pass

# 构造函数例子
class Person():
  # 对Person类进行实例化
  def __init__(self):
    self.name = "nono"
    self.age = 20
    self.address = "abcdefghijklmnopqrstuvwxyz"
    print("In init func")

p = Person()
print("*"*50)

# 构造函数的调用顺序 - 1
# 如果伯伯地面有写构造函数，则自动向上查找 ，直到找到位置
class A():
  pass

class B(A):
  def __init__(self):
    pass

class C(B):
  pass

c = C()
print("*"*50)

# 构造函数的调用顺序 - 2
class A():
  pass

class B(A):
  def __init__(self, name):
    pass

class C(B):
  pass

c = C("aaaa")
print("*"*50)

# 构造函数的调用顺序 - 3
class A():
  pass

class B(A):
  def __init__(self, name):
    pass

class C(B):
  # C 中想扩展B的构造函数
  # 即调用B的构造函数后再添加一些功能
  # 两种方法实现
  # 第一种能过父类名调用
  def __init__(self, name):
    # 首先调用父类构造函数
    B.__init__(self, name)
    # 其次再增加自己的功能
    print("这是C中附加的功能")
  # 第二种，使用super调用
  '''
  def __init__(self, name):
    # 首先调用父类构造函数
    super(C, self).__init__(name)
    # 其次再增加自己的功能
    print("这是C中附加的功能")
  '''

c = C("我是C")
print("*"*50)

# Mixin 案例
class Person():
  name = "llll"
  age = 18

  def eat(self):
    pass
  
  def drink(self):
    pass

  def sleep(self):
    pass

class Teacher(Person):
  def work(self):
    pass

class Student(Person):
  def study(self):
    pass

class Tutor(Teacher, Student):
  pass

t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)
print("*"*50)

class TeacherMixin():
  def work(self):
    pass

class StudentMixin():
  def study(self):
    pass

class TutorM(Person, TeacherMixin, StudentMixin):
  pass

tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)
print("*"*50)

# issubclass
class A():
  pass

class B(A):
  pass

class C():
  pass
# B 是否是 A 的子类
print( issubclass(B, A)) 
print("*"*50)

# isinstance
class A():
  pass

a = A()
print(isinstance(a, A))
print("*"*50)

# hasattr
class A():
  name = "noName"

a = A()
print(hasattr(a, "name"))
print(hasattr(a, "age"))
print("*"*50)

# help
# help(setattr)
