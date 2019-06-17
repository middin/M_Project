
class Student():
  def __init__(self, name="NoName", age=18):
    self.name = name
    self.age = age
  
  def say(self):
    print("My name is {0}".format(self.name))

def sayHello():
  print("hello hello hello ....")

if __name__ == '__main__':
  print("I am 01...")