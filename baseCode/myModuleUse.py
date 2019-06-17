#
'''
常用模块
- calendar
  - 跟日历相关的模块
- time
- datetime
- os
- shutil
- zip
- math
- string
- 上述模块使用先导入，string是特例
- calendar, time, datetime的区别参考中文意思
'''
# calendar 案例
# calendar:  获取一年的日历字符串
# 参数：
# w = 每个日期之间的间隔字符数
# l = 每周所占的行数
# 以= 每个月之间的间隔字符数
import calendar
cal = calendar.calendar(2017)
print(type(cal))
#print(cal)

cal = calendar.calendar(2017, l=0, c=5)
#print(cal)

# isleap: 判断某一年是否闰年
bl = calendar.isleap(2000)
print(bl)

# leapdays: 获取指定年份之间的闰年的个数
cnt = calendar.leapdays(2001,2018)
print(cnt)

# month() 获取某个月的日历字符串
# 格式：calendar.month(年，月)
# 回值： 月日历的字符串
m5 = calendar.month(2019,5)
print(m5)

# monthrange()  获取一个月的周几吞即和天数
# 格式： calendar.monthrange(年，月)
# 回值： 元组（周几开始，总天数）
# 注意：周默认  0~6表示周一到周天
w,t = calendar.monthrange(2017,3)
print(w)
print(t)

# monthcalendar() 返回一个月每天的矩阵列表
# 格式： calendar.monthcalendar(年，月)
# 回值 ：二级列表
# 注意：矩阵中没有天数用０表示 
m = calendar.monthcalendar(2018, 3)
print(type(m))
print(m)

# prcal: print calendar 直接打印日历
cal = calendar.prcal(2018)
# print(cal)

# prmonth() 直接打印整个月的日历
m = calendar.prmonth(2018,5)
# print(m)

# weekday()   获取周几
# 格式：calendar.weekday(年,月,日)
# 回值 ：周几对应的数字
w = calendar.weekday(2018,3,23)
print(w)

'''
time 模块
- 时间戳
  - 一个时间表示，根据不同语言，可以是整数或者浮点数
  - 是从1970年1月1日0时0分0秒到现在经历的秒数
  - 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
  - 32位操作系统能够支持到2038年
- UTC时间
  - UTC又称世界协议时间
- 夏令时
  - 夏令就是在夏天时将时间调快一小时
- 时间元组
  - 一个包含时间内容的普通元组
'''
import time
# 时间模块的属性
# timezone: 当前时区和UTC时间相关的秒数，元夏令时的情况下
# altzone: 获取当前时区和UTC时间相关的秒数，在夏令时的情况下
# daylight: 测试当前是否是夏令时时间状态， 0 表示是
print(time.timezone)
print(time.daylight)

# 得到时间戳
print(time.time())

# 得到当前时间结构
t = time.localtime()
print(t)

# asctime() 返回元组的正常字符串化之后 的时间格式
# 格式: time.asctime（时间元组）
# 返回值 ： 字符串  Tue May 14 14:40:45 2019
t = time.localtime()
tt = time.asctime(t)
print(tt)

# mktime() 使用时间元组获取对应的时间b戳
# 格式： time.mktime(时间元组)
# 返回值 ：浮点数时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(ts)

# clock: 获取CPU时间，3。0~3。3版本之间使用，3。6调用有问题

# sleep: 使程序进入睡眠，n秒后继续


# strftime: 将时间元组转化为自定义的字符串格式
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
# 把时间表示成： 2008 2.23 12：05
t = time.localtime()
ft = time.strftime("%Y年%m月%d日%H时%M分%S秒", t)
print(ft)

'''
datetime 模块
- datetime提供日期和时间的运算和表示
'''
import datetime
# datetime 常见属性
# datetime.date: 一个理想和的日期，提供年月日
dt = datetime.date(2018,3,26)
print(dt)

# datetime.time:提供一个理想和时间，时分秒
# datetime.datetime: 提供日期跟时间组合
# datetime.timedelta: 提供一个时间差，时间长度
from datetime import datetime
'''
常用类方法：
- today
- now
- utcnow
- fromtimestamp: 从时间戳中返回本地时间
'''
dt = datetime(2018,3,26)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))
print("*"*50)

# datetime.timedelta
# 表示一个时间间隔
from datetime import datetime, timedelta
t1 = datetime.now()
print(t1)
print(t1.strftime("%Y-%m-%d %H:%M-%S"))
td = timedelta(hours=1)
print((t1+td).strftime("%Y-%m-%d %H:%M-%S"))
print("*"*50)

# timeit - 时间测量工具
# 测量程序运行时间间隔实验
def p():
  time.sleep(0.6)

t1 = time.time()
p()
print(time.time() - t1)
print("*"*50)

# 生成列表两种方法的比较
# 如果单纯比较生成一个列表的时间，可能很难实现
import timeit
c = '''
sum = []
for i in range(1000):
  sum.append(i)
'''
# 利用timeit调用代码，执行100000次，查看运行时间
t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)
# 测量C代码执行100000次运行结果
t2 = timeit.timeit(stmt=c, number=100000)
print(t1)
print(t2)
print("*"*50)

# timeit 可以执行一个函数，来测量一个函数的执行时间
def doIt():
  num = 3
  for i in range(num):
    print("Repeat for {0}".format(i))

t = timeit.timeit(stmt=doIt,number=10)
print(t)
print("*"*50)

s = '''
def doIt(num):
  for i in range(num):
    print("Repeat for {0}".format(i))
'''
# 执行 doIt(num)
# setup负责把环境变量准备好
# 实际相当于给timeit创造一个小环境
# 在创作的小环境中，代码执行的顺序 大致是
'''
def doIt(num):
    ...
num = 3
doIt(num)
'''
t = timeit.timeit("doIt(num)", setup=s+"num=3", number=10)
print(t)
print("*"*50)

'''
datetime.datetime模块
- 提供比较好用的时间而已
- 类定义
      classDATe。DATe（year， month，day[
        ...
      ]
- 类方法
- 类属性
'''
from datetime import datetime as dt
print(dt.now())

'''
os - 操作系统相关
- 跟操作系统相关，主要是文件操作
- 与系统相关的操作，主要包含在三个模块里
  - os 操作系统目录相关
  - os.path  系统路径相关操作
  - shutil  高级文件操作，目前树的操作，文件赋值，删除，移动
- 路径
  - 绝对路径：总是从概目录上开始
  - 相对路径：基本以当前环境为开始的一个相对的地方

'''
import os
# getcwd()  获取当前的工作目录
# 格式: os.getcwd()
# 返回值：当前工作上当的字符串
mydir = os.getcwd()
print(mydir)

# chdir() 改变当前工作目录
# 格式： os.chdir(路径)
# os.chdir('home/coding')
# mydir.os.getcwd()

# listdir() 获取一个目录中所有子目录和文件的名称列表
# 格式： os.listdir(路径)
# 返回值：所有子目录和文件名称的列表
ld = os.listdir()
print(ld)

# makedirs() 递归创建文件夹
# 格式： os.makedirs(递归路径)
# 递归路径：多个文件夹层层包含的路径就是递归路径，例如 a/b/c
# rst = os.makedirs("dana")
# print(rst)

# system() 运行系统shell命令
# 格式： os.system(系统命令)
# 返回值：打开一个shell或者终端界面
rst = os.system("ls")
# print(rst)

# getenv() 获取指定的系统环境变量值
# 格式：os.getenv("环境变量名")
# 返回值：指定环境变量名对应的值
rst = os.getenv("PATH")

# exit() 退出当前程序
# 格式： exit()

'''
值部分
- os.curdir: current dir, 当前目录
- os.pardir: parent dir, 父目录
- os.sep: 当前系统的路径分隔符
  - Windows： "\"
  - linux: "/"
- os.linesep: 当前系统的换行符号
  - windows: "\r\n"
  - linux: "\n"
- os.name: 当前系统名称
  - windows: nt
  - linux: posix
'''
path = "/home/coding" + "/" + "asdf"
print(path)

# abspath() 将路径转化为绝对路径
# 格式： os.path.abspath('路径')
# 返回值： 路径的绝对路径
import os.path as op
# . 点号，代表当前目录
# .. 双战，代表父目录
# absp = op.abspath(".")
# print(absp)

# basename() 获取路径中的文件名部分
# 格式： os.path.basename(路径)
# 返回值：文件名字符串
# bn = op.basename("/home/coding")
# print(bn)

# join() 将多个路径并合成一个路径
# 格式： os.path.join(路径1， 路径2，...)
# 返回值： 组合之后的新路径字符串
# bn = "/home/coding"
# fn = "aa"
# p = op.join(bn, fn)
# print(p)

# split() 将路径切割为文件夹部分和当前文件部分
# 格式： os.path.split(路径)
# 返回值：路径和文件名组成的元组
# t = op.split("/home/coding/aa")
# print(t)
# d,p = op.split("/home/coding/aa")
# print(d, p)

# isdir() 检测是否是目录
# 格式： os.path.isdir(路径)
# 返回值 ： 布尔值

# exists() 检测文件或者目录是否存在
# 格式： os.path.exists(路径)
# 返回值： 布尔值
# rst = op.isdir("/home/coding/aa")
# e = op.exists("/home/coding/aa")


# shutil 模块
# copy() 复制文件
# 格式：shutil.copy(来源路径，目标路径)
# 返回值：返回目标路径
# 拷贝的同时，可以给文件重命名
import shutil
# rst = shutil.copy("/home/coding/aa", "/home/coding/bb")
# print(rst)

# copy2() 复制文件，保留元数据(文件信息)
# 格式： shutil.copy2(来源路径，目标路径)
# 返回值：返回目标路径
# 注意： copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据

#  copyfile() 将一个文件中的内容复制到另外一个文件当中
# 格式; shutil.copyfile(源路径，目标路径)
# 返回值： 无
# rst = shutil.copyfile("a.txt", "b.txt")
# print(rst)

# mkove() 移动文件/文件夹
# 格式： shutil.move(源文件，目标文件)
# 返回值：目标路径
# rst = shutil.move("/home/coding/aa", "/home/coding/bb")
# print(rst)

'''
归档和压缩
- 归档： 把多个文件或者文件夹合并到一个文件当中
- 压缩： 用算法把多个文件或者文件夹无损或者有损合并到一个文件当中
'''
# make_archive() 归档操作
# 格式： shutil.make_archive("归档后的目录和文件名"， “后缀”， “需要归档的文件夹”)
# 返回值：归档之后的地址

# 得到一个叫做aa.zip的归档文件
# rst = shutil.make_archive("/home/coding/aa","zip", "/home/coding/bb")
# print(rst)

'''
# zip - 压缩包
# 模块名称叫 zipfile
'''
# zipfile.ZipFile(file[,mode[,compression[,allowZip64]]])
# 创建一个ZipFile对象，表示一个zip文件
import zipfile
# zf = zipfile.ZipFile("/home/coding/aa.zip")

# XipFile.getinfo(name):
# 获取zip文档内指定文件的信息，返回一个zipfile.ZipInfor对象，包含文件的详细信息
# rst = zf.getinfo("a.txt")

# ZipFile.namelist()
# 获取zip文档内所有文件的名称列表
# nl = zf.namelist()
# print(nl)

# ZipFile.extractall([path[,member]])
# 解压zip文档中所有文件到当前目录
# rst = zf.extractall("/home/coding/aa")

'''
random
- 随机数
- 所有的随机模块都是伪随机
'''
# random() 获取0~1之间的随机小数
# 格式：random.random()
# 返回值 ： 随机 0~1之间的小数
import random

print(random.random())

# choice() 随机返回序列中的某个值
# 格式： random.choice(序列)
# 返回值 ：序列中的某个值
l = [ str(i)+" haha" for i in range(10)]
rst = random.choice(l)
print(rst)

# shuffle() 随机打乱列表,原地打乱
# 格式： random.shuffle(列表)
# 返回值： 打乱顺序之后的列表
l1 = [i for i in range(10)]
random.shuffle(l1)
print(l1)

# randint(a,b): 返回一个a到b之间的随机整数，包含a和b
print(random.randint(0,100))

# log 模块
# https://www.cnblogs.com/yyds/p/6901864.html


# 高阶函数
# zip
# - 把两个可迭代内容生成一个可迭代的tuple元素类
# zip 案例
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]
z = zip(l1, l2)
print(type(z))
print(z)
for i in z:
    print(i)

l1 = ["wang", "myue", 'yyt']
l2 = [89, 23, 78]
z = zip(l1, l2)
for i in z:
    print(i)

# enumerate
# - 跟zip功能比较像
# - 对可迭代对象里的每一元素，配上一个索引，然后索引和内容构成tuple类型
l1 = [11,22,33,44,55]  
em = enumerate(l1)
l2 = [i for i in em]
print(l2)

em = enumerate(l1, start=100)
l2 = [i for i in em]
print(l2)

# collections 模块
# - namedutple
# - deque
# namedtuple
# - tuple类型
# - 是一个可命名的tuple
import collections
Point = collections.namedtuple("Point", ['x', 'y'])
p = Point(11,22)
print(p.x, p.y)
print(p[0])

Circle = collections.namedtuple("Circle", ['x', 'y', 'r'])
c = Circle(100, 150, 50)
print(c)
print(type(c))
# 检测以下namedtuple属于谁的子类
isinstance(c, tuple)

# deque
# - 比较方便的解决了频繁删除插入带来的效率问题
from collections import deque
q = deque(['a', 'b', 'c'])
print(q)
q.append('d')
print(q)
q.appendleft('x')
print(q)

# defaultdict
# - 当直接读取dict不存在的属性时，直接返回默认值 
d1 = {"one":1, "two":2, "three":3}
print(d1["one"])
#print(d1["four"])

from collections import defaultdict
func = lambda: "lindana"
d2 = defaultdict(func)
d2["one"]=1
d2["two"]=2
print(d2["one"])
print(d2["four"])

# Counter
# - 统计字符串个数
from collections import Counter
# 需要括号里内容为可迭代
c = Counter("asdfasdfasdfg")
print(c)

s = ["liudana", "love", "love", "love", "asdf"]
c = Counter(s)
print(c)