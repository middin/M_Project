#收集参数混合调用实例
def studen(name, age, hobby="没有", *args, **kwargs):
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

studen(name, age, hobby="游泳", "lily", hobby2="cooking", hobby3="chatting")