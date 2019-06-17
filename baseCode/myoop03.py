#

'''
变量的三种用法
'''
class A():
  def __init__(self):
    self.name = "haha"
    self.age = 18

a = A()
# 属性的三种用法
# 1。 赋值
# 2。 读取
# 3。 删除
a.name="dana"
print(a.name)
del a.name
# print(a.name)

# 类属性 property
# 应用场景：
# 对变量除了普通 的有三种操作，还想增加一些附加的操作，那么可以通过property完成
class A():
  def __init__(self):
    self.name = "haha"
    self.age = 18
  
  # 此功能，是对类变量进行读取操作时应该执行的函数
  def fget(self):
    print("be readed ...")
    return self.name

  # 模拟的是对变量进行写操作r时执行的功能
  def fset(self, name):
    print("be written...")
    self.name = "学院：" + name
    #self.name = name

  # fdel 模拟的是删除变量时进行的操作
  def fdel(self):
    pass

  name2 = property(fget, fset, fdel, "这是一个property的例子")

a = A()
print(a.name)
print(a.name2)