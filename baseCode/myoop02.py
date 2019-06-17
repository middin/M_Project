# 
'''
类的成员描述符(属性)
- 类的成员让所有他无法是为了在类中对类的成员属性进行相关操作而创建的一种方式
  - get: 获取属性的操作
  - set: 修改或者添加属性操作
  - delete: 删除属性操作
- 如果想使用类的成员描述符，三种方法：
  - 使用类实现描述器
  - 使用属性修饰符
  - 使用 property 函数
    - property 函数很简单
    - propertyr(fget, fset, fdel, doc)
  - 案例参考  属性案例 -2
- 无论哪种修饰符都是为了对成员属性进行相应的控制
  - 类的方式： 适合多个类中的多个属性共用一个描述符
  - property： 使用当前类中使用，可以控制一个类中多个属性
  - 属性修饰符： 使用于当前类中使用，控制一个类中的一个属性

类的内置属性
    __dict__ : 以字典的方式显示类的成员组成
    __doc__ : 获取类的文档信息
    __name__ : 获取类的名称,如果在萨夫尼克使用，获取模块的名称
    __bases__ : 获取某个类的所有父类，以元组方式显示

类的常用魔术方法
- 魔术方法就是不需要人为调用的方法，基本是在特定的时刻自动触发
- 魔术方法的统一特征： 方法名被前后各两个下划线包裹
- 操作类
  - __init__ ： 构造函数
  - __new__ : 对象实例化方法，此函数较特殊，一般不需要使用
  - __call__ :对象当函数使用时触发
  - __str__ : 当对象被当做字符串使用时调用
  - __repr__: 返回字符串，跟__str__具体区别
- 描述符相关
  - __set__
  - __get__
  - __delete__
- 属性操作相关
  - __getattr__: 访问一个不存在的属性时触发
  - __setattr__: 对成员属性进行设置时触发
    - 参数： 
      - self 用来获取当前对象
      - 被设置的属性名称，以字符串形式出现
      - 需要对属性名称设置的值
    - 作用： 进行属性设置时进行验证或者修改
    - 注意： 在该方法中不能对属性直接进行赋值操作，否则死循环
    - 参考案例 __setattr__ 案例
- 运算分类相关魔术方法
  - __gt__: 进行大于判断 时触发的函数
    - 参数
      - self
      - 第二个参数是第二个对象
      - 返回值可以是任意值，推荐返回布尔值
      - 案例 __gt__ 案例

类和对象的三种方法
- 实例方法：
  - 需要实例化对象才能使用的方法，使用过程中可能 需要带上对象的其它对旬的方法完成
- 静态方法
  - 不需要实例化，通过类直接访问
- 类方法
  - 不需要实例化
- 参看案例  三种方法案例
- 三个方法的区别

抽象类
- 抽象方法：没有具体实现内容的方法成为抽象方法
- 抽象方法的主要意义是规范了子类的行为和接口
- 抽象类使用需要借助abc模块
        import abc
- 抽象类：包含抽象方法的类叫抽象类，通常成为ABC类
- 抽象类的使用
    - 抽象类可以c包含抽象方法，也可以包含具体方法
    - 抽象类中可以有方法也可以有属性
    - 抽象类不允许直接实例化
    - 必须继承才可以使用，且继承的子类必须实现所有继承来的抽象方法
    - 假定子类没有实现所有o继承的抽象方法，则子类也不能实例化
    - 抽象类的主要作用是设定类的标准，以便于开发是具有统一规范

自定义类
- 类其实是一个类定义和各种方法的自由组合
- 可以定义类和函数，然后自己通过类直接赋值
- 可以借助于MethodType实现
- 借助于Type实现
- 利用元类实现 - MetaClass
    - 元类是类
    - 备用来创建其它类
'''
# 属性案例 -1 
# 创建Student类，描述学生类
# 学生具有Student.name属性
# 但name格式并不统一
class Student():
  def __init__(self, name, age):
    self.name = name
    self.age = age

    # 如果不想修改代码，可如下操作
    self.setName(name)
  
  # 介绍自己
  def intro(self):
    print("Hi, my name is {0}".format(self.name))
  
  def setName(self, name):
    self.name = name.upper()

s1 = Student("liu", 19)
s2 = Student("mich", 24)
s1.intro()
s2.intro()
print("*"*50)

# 属性案例 - 2
# 定义一个Person类，具有name,age属性
# 对任意输入的t姓名，都用大写方式保存
# 年龄，内部统一整数保存
# x = property(fget, fset, fdel, doc)
class Person():
  """
  asdfasdfasdfasdfasdf
  """
  def fget(self):
    return self._name * 2
  
  def fset(self, name):
    self._name = name.upper()
  
  def fdel(self):
    self._name = "NoName"
  
  name = property(fget, fset, fdel, "对name进行操作")

p1 = Person()
p1.name = "lily"
print(p1.name)
print("*"*50)

#类的内置属性
print(Person.__dict__)
print(Person.__doc__)
print(Person.__bases__)
print("*"*50)

# __call__ 实例
# 将类对象当函数调用
class A():
  def __init__(self, name=0):
    print("被调用了")
  
  def __call__(self):
    print("又被调用了")

a = A()
a()
print("*"*50)

# __str__ 实例
# 将类对象当函数调用
class A():
  def __init__(self, name=0):
    print("被调用了")
  
  def __call__(self):
    print("又被调用了")

  def __str__(self):
    return "asdfasdf"

a = A()
print(a)
print("*"*50)

# __getattr__ 实例
# 将类对象当函数调用
class A():  
  name = "NoName"
  age = 18

  def __getattr__(self, name):
    print("没找到")
    print(name)


a = A()
print(a.name)
print(a.addr)
print("*"*50)

# __setattr__ 案例
class Person():
  def __init__(self):
    pass
  
  def __setattr__(self, name, value):
    print("设置属性： {0}".format(name))
    # 下面语句会导致问题，死循环
    # self.name = value
    # 为了避免死循环，规定统一调用父类
    super().__setattr__(name,value)

p = Person()
print(p.__dict__)
p.age = 18
print("*"*50)

# __git__ 案例
class Student():
  def __init__(self, name):
    self.name = name
  
  def __gt__(self, obj):
    print("hah, {0} 会比 {1} 大吗？".format(self, obj))
    print("hah, {0} 会比 {1} 大吗？".format(self.name, obj.name))
    return self.name > obj.name

stu1 = Student("one") 
stu2 = Student("two")
print(stu1 > stu2)
print("*"*50)

# 三种方法案例
class Person():
  # 实例方法
  def eat(self):
    print(self)
    print("eating...")
  
  # 类方法
  # 类方法的第一个参数，一般命名为cls，区别于self
  @classmethod
  def play(cls):
    print(cls)
    print("laying...")
  
  #静态方法
  #不需要用第一个参数表示自身或者类
  @staticmethod
  def say():
    print("say....")

yy = Person()
# 实例方法
yy.eat()
# 访问类方法
Person.play()
yy.play()
# 访问静态方法
Person.say()
yy.say()
print("*"*50)

# 抽象 实例
class Animel():
    def sayHello(self):
        pass

class Dog(Animel):
    def sayHello(self):
        print("闻下对方的味道")

class Person(Animel):
    def sayHello(self):
        print("握手")

d = Dog()
d.sayHello()

p = Person()
p.sayHello()
print("*"*50)

# 抽象类的实现    实例
'''
import abc

# 声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    #定义类抽象方法
    @abc.adstractclassmethod
    def drink():
        pass
    
    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    # 具体方法
    def sleep(self):
        print("sleeping ...")
'''

# 函数名可以当变量使用
def sayHello(name):
    print("{0} 好吗？".format(name))

sayHello("yy")
liumang = sayHello
liumang("xx")
print("*"*50)

# 自己组装一个类
class A():
    pass

def say(self):
    print("saying ...")

class B():
    def say(self):
        print("saying....B")
say(9)
A.say = say
a = A()
a.say()

b = B()
b.say()
print("*"*50)

# 组装类 实例   2
# 自己组装一个类
from types import MethodType
class A():
    pass

def say(self):
    print("saying ...")

a = A()
# MethodType 通过此把具体方法绑定到类里面
a.say = MethodType(say, A)
a.say()
print("*"*50)

# type 实例  利用type造一个类
# 先定义类应该好玩的人成员函数
def say(self):
    print("saying........")

def talk(self):
    print("takling.......")

# 用type创建一个类
A = type("AName", (object,), {"class_say": say, "class_talk": talk})

# 然后可以像正常访问一样使用类
a = A()
a.class_say()
a.class_talk()
print("*"*50)

# 元类演示
# 元类写法是固定的，必须继承自type
# 元类一般命名以MetaClass结尾
class TulingMetaClass(type):
    # 注意以下写法
    def __new__(cls, name, bases, attrs):
        # 自己的业务代码
        print("haha, 我是元类")
        attrs['id'] = '0000'
        attrs['addr'] = 'bjhdgzfxvl12n'
        return type.__new__(cls, name, bases, attrs)

# 元类定义完就可以使用，使用注意写法
class Teacher(object, metaclass=TulingMetaClass):
    pass

t = Teacher()
print(t.__dict__)
print(t.id)
