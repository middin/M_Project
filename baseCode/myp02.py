#

# # 案例 1
# import myp01

# stu = myp01.Student("xiaojin", 20)
# stu.say()

# myp01.sayHello()
# print("*"*50)

# # 调用第三方包， 案例 2
# import importlib
# tuling = importlib.import_module("01")

# stu = tuling.Student("lili", 100)
# stu.say()
# print("*"*50)

# #  案例 3
# import myp01 as mp

# stu = mp.Student("yy", 11)
# stu.say()
# print("*"*50)

# # 案例 4
# from myp01 import Student, sayHello

# stu = Student()
# stu.say()
# sayHello()
# print("*"*50)

# # 案例 5
# from myp01 import *

# sayHello()
# stu = Student("xxx", 44)
# stu.say()
# print("*"*50)

# # 案例 ６
# import sys

# print(type(sys.path))
# print(sys.path)

# for p in sys.path:
#   print(p)

# print("*"*50)

# # 案例 7
# import pkg01

# pkg01.inInit()
# print("*"*50)

# # 案例 8
# import pkg01.p01

# stu = pkg01.p01.Student()
# stu.say()
# print("*"*50)

# 案例 9
# from pkg01 import *

# inInit()
# # 报错
# # stu = Student("zzzzzzzz", 2000)  
# # stu.say()

# 案例 10
from pkg02 import *

stu = p01.Student()
stu.say()