#
'''
pycharm
- markdown 插件
- vim 插件

OOP-PYTHON面向对象
- 面向对象编程
    - 基础
    - 公有/私有
    - 继承
    - 组合、Minxi
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数

1。面向对象概述(ObjectOriented, OO)
- OOP思想
    - 接触到任意一个任务，首先想到的是任务这个案例微软构成，是由模型构成的
- 几个名词
    - OO: 面向对象
    - OOA: 面向对象的分析
    - OOD: 面向对象的设计
    - OOI: XXX的实现
    - OOP: xxx的编程
    - OOA->OOD->OOI: 面向对象的实现过程
- 类和对象的概念
  - 类：抽象名词，代表一个集合，共性的事物
  - 对象：具象的事物，单个个体
  - 类跟对象的关系：
    - 一个具象，哇哥哥类事物的某一个个体
    - 一个是抽象，代表的是一大类事物 
- 类中的内容，应该具有两个内容
    - 青蛙事物的特征，叫做属性（变量）
    - 青蛙事物功能和动作，称为成员方法
2。类的基本实现
  - 类的命名
    - 遵守变量命名的规范
    - 大驼峰(由一个或者多个单词构成，每个单词首字母大写，单词跟单词u直接相连)
    - 尽量避开跟系统命名身为女人命名
  - 如何声明一个类
    - 必须用class 关键字
    - 类由属性和方法构成，其它不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有，允许使用None
    - 案例
  - 实例化类
      变量= 类名（） # 实例化了一个对象
  - 访问对象成员
    - 使用点操作符
        obj.成员属性名称
        obj.成员方法
  - 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员检查
          # dict前后各有两个下划线
          obj.__dict__
    - 类所有的成员
          # dict前后各有两个下划线
          class_name.__dict__
3. 类和对象的成员分析
- 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象
- 独享存储成员是存储在当前对象中
- 对象访问一个成员是，如果对象中没有该成员，尝试访问类中的同名成员，如果对象中有此成员，一定使用对象中的成员
- 创建对象的时候，类中的成员不会放对象当中，而是得到个空对象，没有成员
- 通过对象对类中的成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员

4。关于self
- self 在对象的方法中表示 妆前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前的第一个参数中
- self并不是关键字，只是一个用于接受对象的普通参数，理论上可以用任何一个普通变量名代替
- 方法中有self形参的方法成为非绑定类的方法，可以通过对象访问，没有self的的是绑定类的方法，只能通过类访问
- 使用类访问绑定类的方法时，如果 类方法中需要访问当前类的成员，可以通过__class__.成员名来访问

5.面向对象的三大特性
- 封装
- 继承
- 多态

5.1 封装
- 封装就是对对象的成员进行访问限制
- 封装的三个t级别：
  - 公开： public
  - 保护： protected
  - 私有： private
  - public, private, protected 不是关键字
- 判断对象的位置
  - 对象内部
  - 对象外部
  - 子类中

- 私有
    - 私有成员是最高级别是封装，只能在当前 类或者对象中访问
    - 在成员前面添加两个下划线即可
        class Person():
          # name 是共有成员
          name = "lili"
          # __age 就是私有成员
          __age = 18
    - Python的私有不是真私有，是一种成为name mangling的改名策略
    - 可以使用对象._classname_attributename访问
- 受保护的封装 protected
    - 受保护的封装是将对象成员进行一定级别的封装，然后，在类中或者子类中都可以进行访问，但是在外都不可以
    - 封装方法，在成员名称前添加一个下划线
- 公开的，公共的 public
    - 公共的封装实际对成员没有任何操作，任何地方都可以访问

5.2 继承
- 继承就是一个类可以获得另外一个类中的成员属性和成员方法
- 作用： 减少代码，增加代码的利用功能，同时可以设置类怀类之间的关系
- 继承n与被继承的概念：
    - 被继承的类叫父类，基类，超类
    - 用于继承的类，叫自类，派生类
    - 继承与被继承一定存在一个 is-a 关系
- 继承的语法
- 继承的特征
    - 所有的类都继承自object类，即所有的类都是object的子类
    - 子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
    - 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
    - 子类中可以定义独有的成员属性和方法
    - 子类中定义的成员和父类成员如果相同，则优先使用子类成员
    - 子类如果想扩充父类方法，可以在定义新方法的同时访问父类成员来进行码复用
    可以使用 父类名.父类成员 的格式来调用父类成员，也可以使用 super()。父类成员来调用
- 继承变量函数的查找顺序问题
    - 优先查找自己的变量
    - 没有则查找父类
    - 构造函数如果本类中没有定义，则自动调用父类构造函数
    - 如果本类有定义，则不在继续向上查找
- 构造函数
    - 是一类特殊的函数，在类进行实例化之前进行调用
    - 如果定义了构造函数，则实例化时使用构造函数，不查找父类构造函数
    - 如果没定义，则自动查找 父类构造函数
    - 如果子类没定义，父类的构造函数带参数，则构造对象时的参数应该按父类参数构造
- super
    - super 不是一个关键字
    - super 的作用是获取 MRO（MethodResolutionOrder)列表中的第一个类
    - super 与父类直接没有任何实质性的关系，但通过super可以高用到父类
    - super 使用两个方法
        - 在构造参数中调用父类的构造函数
        - 
'''
# 定义一个空类
class Student():
  pass

# 定义一个对象
mingyue = Student()

class PythonStudent():
  # None给不确定的变量赋值
  name = None
  age = 18
  course = "Python"

  # 需要注意： 缩进层级； 系统默认的一个self参数
  def doHomeWork(self):
    print("I 在做作业")
    return None

# 对象实例化
yy = PythonStudent()
print(yy.name)
print(yy.age)
yy.doHomeWork()

# print(PythonStudent.__dict__)
print("*"*50)

# 实例2
class A():
  name = "dana"
  age = 18

  def say(self):
    self.name = "aaa"
    self.age = 200

# 此案例说明
# 类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下
# 指向同一个变量
print(A.name)
print(A.age)
print("*"*30)
print(id(A.name))
print(id(A.age))
print("*"*30)
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print("*"*50)


print(A.name)
print(A.age)
print(id(A.name))
print(id(A.age))
print("*"*30)
a = A()
# 查看类内所有的属性
print(A.__dict__)
print(a.__dict__)  # 输出 {}
a.name = "yaona"
a.age = 16
print(a.__dict__)
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print("*"*50)



# 实例3
class Student():
  name = "dana"
  age = 18

  def say(self):
    self.name = "aaa"
    self.age = 200
    print("name is {0}".format(self.name))
    print("age is {0}".format(self.age))
  
  def sayAgain(s):
    print("name is {0}".format(s.name))
    print("age is {0}".format(s.age))

yy = Student()
yy.say()
yy.sayAgain()
print("*"*50)


# 实例4
class Teacher():
  name = "adna"
  age = 19
  
  def say(self):
    self.name = "aaa"
    self.age = 200
    print("name is {0}".format(self.name))
    # 调用类的成员变量需要用__class__
    print("age is {0}".format(self.age))

  def sayAgain():
    print(__class__.name)
    print("hhhhhhhhhhhhhh")

t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.sayAgain()
print("*"*50)

# 实例5
class A():
  name = "lijli"
  age = 14

  def __init__(self):
    self.name = "aaaa"
    self.age = 100

  def say(self):
    print(self.name)
    print(self.age)

class B():
  name = "BBBBB"
  age = 94

a = A()
a.say()
# 此时，self被a替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)
# 此时，传入的是类实例B，因为B具有name和age属性,所以不会报错
A.say(B)
# 以上代码，利用了鸭子模型
print("*"*50)

# 实例6
class Person():
  # name 是共有成员
  name = "lili"
  # __age 就是私有成员
  __age = 18

p = Person()
# name 是仅有变量
print(p.name)
#__age是私有变量
#print(p.__age)

print(Person.__dict__)
p._Person__age = 19
print(p._Person__age)
print("*"*50)
#####################################################################
# 继承的语法
class Person():
    name = "noname"
    age = 20
    __score = 0 # 考试成绩是秘密，只要自己知道
    _petname = "set" # 小名，是保护的，子类可以用，但不能公用

    def sleep(self):
        print("sleeping ...")
# 父类写在括号里面
class Teacher(Person):
    teacher_id = 10
    def make_test(self):
        print("attention")

t = Teacher()
t.sleep()
print(t.name)
print(Teacher.name)
# 受保护不能外部访问，为啥这里可以
print(t._petname)
# 私有访问问题
# print(t.__score)
print(t.teacher_id)
t.make_test()
print("*"*50)

# 子类p和父类定义同一个名称变量，则优先使用子类本身
class Person():
    name = "noname"
    age = 20
    __score = 0 # 考试成绩是秘密，只要自己知道
    _petname = "set" # 小名，是保护的，子类可以用，但不能公用

    def sleep(self):
        print("sleeping ...")


# 父类写在括号里面
class Teacher(Person):
    teacher_id = "9527"
    name = "nana"
    def make_test(self):
        print("attention")

t = Teacher()
print(t.name)
print("*"*50)

# 子类扩充父类功能的案例
class Person():
    name = "noname"
    age = 20
    __score = 0 # 考试成绩是秘密，只要自己知道
    _petname = "set" # 小名，是保护的，子类可以用，但不能公用

    def sleep(self):
        print("sleeping ...")

    def work(self):
        print("make some money")

# 父类写在括号里面
class Teacher(Person):
    teacher_id = "9527"
    name = "nana"

    def make_test(self):
        print("attention")
    
    def work(self):
        # 扩充父类的功能只需要调用父类十一日函数 super
        # Person.work(self)
        super().work()
        self.make_test()

t = Teacher()
t.work()
print("*"*50)

# 构造函数的概念
class Dog():
    # 每次实例化时第一个被调用
    def __init__(self):
        print("I ma init in dog")
    
kak = Dog()
print("*"*50)

# 继承中的构造函数
class Animal():
    def __init__(self):
        print("Animal")

class PaxingAni(Animal):
    def __init__(self):
        print("Paxing Dongwu")

class Dog(PaxingAni):
    # 每次实例化时第一个被调用
    def __init__(self):
        print("I ma init in dog")

class Cat(PaxingAni):
    pass

# 实例化的时候，自动调用了Dog的构造函数，因找到本类中的构造函数，则不在查找 父类的构造函数
kak = Dog()

c = Cat()
print("*"*50)

# 继承中的构造函数 -3 
class Animal():
    def __init__(self):
        print("Animal")

class PaxingAni(Animal):
    def __init__(self, name):
        print("Paxing Dongwu {0}".format(name))

class Dog(PaxingAni):
    # 每次实例化时第一个被调用
    def __init__(self):
        print("I ma init in dog")

class Cat(PaxingAni):
    pass

# 实例化的时候，自动调用了Dog的构造函数，因找到本类中的构造函数，则不在查找 父类的构造函数
kak = Dog()

# c = Cat() # 出错，参数不匹配
c = Cat("mimi")
print("*"*50)

print(type(super))
help(super)
print("*"*50)


