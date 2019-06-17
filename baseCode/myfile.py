#

'''
文件
- 长久保存信息的一种数据信息集合
- 常用操作
  - 打开关闭(文件一旦打开，需要关闭操作)
  - 读写内容
  - 查找
open 函数
- open 函数负责打开文件，带有很多参数
- 第一个参数： 必须有，文件的路径和名称
- mode:青蛙文件用什么方式打开
  - r: 以只读方式打开
  - w: 写方式打开，会覆盖以前的内容
  - x：创建方式打开，如文件已经存在，报错
  - a: append方式，以追加的方式p对文件内容进行写入
  - b: binary方式，二进制方式写入
  - t: 文件方式打开
  - +: 可读写
'''
# 打开文件，用写的试
f = open(r"test01.txt", 'w')
f.close()
# 此案例说明，以写方式打开文件，默认是如果没有文件，则创建

# with 语句
# - with 语句使用的技术是一种成为上下文字处理协议技术(ContextMaanagementProtocal)
# - 自动判断文件的作用域，自动关闭不在使用的打开的文件句柄
# with 语句案例 1
with open(r"test01.txt", "r") as f:
  pass
  # 下面语句块c开始对文件进行操作
  # 在本模块中不需要在使用close关闭文件 f

# with 案例 2
with open(r"test01.txt", "r") as f:
  # 按行读取内容
  strline = f.readline()
  # 此结构保证能够完整读取文件直到结束
  while strline:
    print(strline)
    strline= f.readline()

# list 通用打开的文件作为参数，把文件内每一行内容作为一个元素
with open(r"test01.txt", "r") as f:
  # 以打开的文件f作为参数，创建列表
  l = list(f)
  for line in l:
    print(line)

# read 是按字符读取文件内容
# 允许输入参数决定读取几个字符，如果没有指定，从当前位置读取到结尾
# 否则，从当前位置读取指定个数字符
with open(r"test01.txt", "r") as f:
  strChar = f.read() # f.read(1) 每次读取一个
  print(len(strChar))
  print(strChar)

# seek (offset, from)
# - 移动文件的读取位置，也叫读取指针
# - form的取值范围
#     - 0: 从文件头开始偏移
#     - 1：从文件当前位置开始偏移
#     - 2：从文件末尾开始偏移
# - 移动的单位是字节(byte)
# - 一个汉字由若干个字节组成
# - 返回文件指针对应当前位置
# seek 案例 1
# 打开文件后，从第5个字节处开始读取
with open(r"test01.txt", "r") as f:
  # seek 移动单位是字节
  f.seek(6, 0)
  strChar = f.read()
  print(strChar)

# 打开文件，三个字符一组读出内容，每读一次，休息一秒钟
import time

with open(r"test01.txt", "r") as f:
  # read 参数的单位是字符，一个汉字京是一个字符
  strChar = f.read(3)
  while strChar:
    print(strChar)
    # sleep 参数单位是钞
    time.sleep(1)
    strChar = f.read(3)

# tell函数：用来显示文件读写指针的当前位置
# tell 返回数字的单位是byte
# read 是以字符为单位
with open(r"test01.txt", "r") as f:
  strChar = f.read(3)
  pos = f.tell()
  while strChar:
    print(pos)
    print(strChar)
    strChar = f.read(3)
    pos = f.tell()

# 文件的写操作 - write
# - write(str): 把字符串写入文件
# - writelines(str): 把字符串p按行写入文件
# - 区别
#     - write 函数参数只能是字符串
#     - writelines:参数可以是字符串，也可以是字符序列
# write 案例 1
# a 以追加方式打开
with open(r"test01.txt", "a") as f:
  f.write("生活不仅有眼前的苟且\n还有远方的苟且")

# writelines 案例
# writelines 写入很多行，参数可以是list格式
with open(r"test01.txt", "w") as f:
  seq = ["生活不仅有眼前的苟且\n", "还有远方的苟且"]
  f.writelines(seq)

'''
持久化 - pickle
- 序列化（持久化，落地）：把程序运行中的信息保存在磁盘上
- 反序列化： 序列化的逆过程
- pickle: python 提供的序列化模块
- pickle.dump: 序列化
- pickle.load: 反序列化
'''
# 序列化 案例 1
import pickle
age = 19
with open(r"test01.txt", "wb") as f:
  pickle.dump(age, f)

# 反序列化案例 1
with open(r"test01.txt", "wb") as f:
  age = pickle.load(f)
  print(age)

# 序列化案例 2
age = [19, 'linudana', 'i love china',[185, 67]]
with open(r"test01.txt", "wb") as f:
  pickle.dump(age, f)
# 反序列化案例 2
with open(r"test01.txt", "wb") as f:
  a = pickle.load(f)
  print(a)

# 持久化- shelve
# - 持久化工具
# - 类似字典，用kv对保存数据，存取方式跟字典也类似
# - open, close  成对出现
# shelve 定稿案例
import shelve
# 打开文件，  shv相当于一个字典
shv = shelve.open(r'shv.db')
shv['one'] = 1
shv['two'] = 2
shv.close()
# shelve 自动创建的不仅仅是一个shv.db文件，还名手其它格式文件

# shelve 读取案例
shv = shelve.open(r'shv.db')
print(shv['one'])
shv.close()

# shelve 特性
# - 不支持多个应用并行写入
#   - 解决方法：open时，可以使用flag=r
# - 写回问题
#   - shelvep在写入情况下不会等待持久化对象进行任何修改
#   - 解决方法： 强制写回： writeback=True
# 案例 1
shv = shelve.open(r'shv.db', flag='r')
try:
  k1 = shv['one']
  print(k1)
finally:
  shv.close()

# 案例 2
shv = shelve.open(r'shv.db')
try:
  shv['one'] = {"eins":1, "zwei":2, "drei":3}
finally:
  shv.close()
shv = shelve.open(r'shv.db')
try:
  one = shv['one']
  print(one)
finally:
  shv.close()

# shelve 忘记写回，需要使用强制写回
# 案例 3 -1 
shv = shelve.open(r'shv.db')
try:
  one = shv['one']
  print(one)
  # 此时，一旦shelve关闭，则内容还是在于内存中，没有写回数据库
  one["eins"]=100
finally:
  shv.close()
shv = shelve.open(r'shv.db')
try:
  one = shv['one']
  print(one)
finally:
  shv.close()

# 案例 3-2
shv = shelve.open(r'shv.db', writeback=True)
try:
  one = shv['one']
  print(one)
  one["eins"]=100
finally:
  shv.close()
shv = shelve.open(r'shv.db')
try:
  one = shv['one']
  print(one)
finally:
  shv.close()

# shelve 使用 with 管理上下文环境
with shelve.open(r'shv.db', writeback=True) as shv:
  one = shv['one']
  print(one)
  one["eins"]=1000
with shelve.open(r'shv.db') as shv:
  one = shv['one']
  print(one)









