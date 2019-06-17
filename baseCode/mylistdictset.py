#

"""
汉诺塔问题
- 规则
  - 每次移动一个，小在上，大在下
- 方法
  - n = 1, 直接移动到C上， A->C
  - n = 2
    - A -> B
    - A -> C
    - B -> C
  - n = 3
    - 把A上的两个盘子，通过C移动到B，调用递归实现
    - 把A上剩下的最大盘子移动到C, A->C
    - 把B上两个盘借助A移动到Cf上去， 调用递归函数
  - n = n
    - 把A上的n-1个盘子，借助于C，移动到B上去，调用递归
    - 把A上的最大盘子，也是唯一一个，移动到CH , A->C
    - 把B上的n-1个盘子，借助于A,移动到C上， 调用递归
"""
def hano(n, a, b, c):
  '''
  n: 代表几个盘子
  a: 代表第一个盘子
  b: 代表第二个盘子
  c: 代表第三个盘子
  '''
  if n == 1:
    print(a, "-->", c)
    return None
  
  if n == 2:
    print(a, "-->", b)
    print(a, "-->", c)
    print(b, "-->", c)
    return None
  
  hano(n-1, a, c, b)
  print(a, "-->", c)
  hano(n-1, b, a, c)

a = 'A'
b = 'B'
c = 'C'
hano(3, a, b , c)

'''
List 列表
- del: 删除命令
'''
a = [1,2,3,4,5]
print(id(a))
del a[2]
print(id(a))
print(a)

# 列表相加
a = [1,2,3,4,5]
b = [5,6,7,8,9]
c = a+b
print(c)

# 使用乘号操作列表
# 相当于把n个列表接在一起
a = [1,2,3,4,5]
b = a*2
print(b)

# 成员资格运算
# 判断一个元素是否在列表里面边
a = [1,2,3,4,5]
b = 8
c = b in a  # c值值为一个布尔值
print(c)
c = b not in a
print(c)

'''
链表的遍历
- for
- while
'''
a = [1,2,3,4,5]
for i in a:
  print(i)

b = ['I', 'love', 'china']
for i in b:
  print(i)

# range
for i in range(1,3):
  print(i)
print(type(range))

# while 循环访问 List
# 一般不用while遍历list
a = [1,2,3,4,5]
length = len(a)
index = 0
while index < length:
  print(a[index])
  index += 1

# 双层链表或嵌套列表
a = [['noe', 1], ['two', 2], ['three', 3]]
for k,v in a:
  print(k, "--", v)


# 列表内涵： list conten
# 通过简单方法创作列表
a = ['a', 'b', 'c']
# 用list a创建一个 list b
# 对于a中的元素，逐个放入b中
b = [i for i in a]
print(b)

# 过滤list中的内容放入新列表
a = [x for x in range(1,10)]
# 把a中所有偶数生成列表b
b = [m for m in a if m%2 == 0]
print(b)

# 列表生成式可以嵌套
a = [i for i in range(1,10)]
print(a)

b = [i for i in range(100, 1000) if i%100 == 0]
# 列表嵌套
c = [m+n for m in a for n in b]
'''
# 上面代码类同如下
for m in a:
  for n in b:
    m+n
'''
print(c)

# 列表函数
# len: 求列表长度
a = [x for x in range(8, 100)]
print(len(a))

# max: 求列表中最大值
# min:
print(max(a))

b = ['man', 'film', 'python']
print(max(b))

# list: 将其它是他爱人数据转换成list
s = 'i love china'
print(list(s))

#####################################################################

def a(n):
  n[2] = 300
  print(n)
  return None

def b(n):
  n+=100
  print(n)
  return None

an = [1,2,3,4,5]
bn = 9

print(an)
a(an)
print(an)

print(bn)
b(bn)
print(bn)

############################################################################

# 关于列表的函数
l = ['a', 'i love', 45, 377, 5+2]
print(l)

# append 插入一个内容，在末尾添加
a = [ i for i in range(1,5)]
print(a)
a.append(100)
print(a)

# insert; 指定位置插入
# insert(index, data), 输入位置是index前面
a.insert(3, 666)
print(a)

# 删除
# del 删除指定位置
# pop 从列表拿出一个元素，即把最后一个元素好出来
last_ele = a.pop()
print(last_ele)
print(a)

# remove: 删除指定数值
# 如果删除值 不在列表中，则报错
# 即 ， 删除list指定数值使用try...catch语句，或者先行判断再执行
print(id(a))
a.remove(666)
print(a)
print(id(a))

# clear: 清空
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))
# 如果不需要保存列表，则如下清理
# a = [1,2,3,]
# a = []
a = []
print(id(a))

# reverse: 原地翻转
a = [1,2,3,4,5]
print(a)
print(id(a))
a.reverse()
print(a)
print(id(a))

# extend: 扩展列表，两个列表， 把一个直接拼接到后一个上
a = [1,2,3,4,5]
b = [6,7,8,9]
print(a)
print(id(a))
a.extend(b)
print(a)
print(id(a))

# count: 查找列表中指定元素的个数
a_cnt = a.count(1)
print(a_cnt)

# copy: 拷贝，浅拷贝
a = [1,2,3,4,5,666]
print(a)
# list 类型，简单赋值操作，是传地址
b = a.copy() # b = a 与 b = a.copy的区别
b[3] = 777
print(a)
print(b)

# 深拷贝跟浅拷贝的区别
# copy 函数是个浅拷贝函数，即只拷贝一层内容
# 深f拷贝需要使用特定工具
a = [1,2,3, [10,20,30]]
b = a.copy()
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
a[3][2] = 666
print(a)
print(b)

#####################################################################
'''
元组 - tuple
- 元组可以看成是一个不可更改的list
'''
# - 元组的创建
t = ()
print(type(t))
# 创建一个只有一个值的元x组
t = (1,)
print(type(t))
print(t)

t = 1,
print(type(t))
print(t)

# 创建多个值 的元素
t = (1,2,3,4)
print(t)

t = 1,2,3,4
print(t)

# 使用其它结构创建
l = [1,2,3,4,5]
t = tuple(l)
print(t)

'''
元组的特性
- 是序列表，有序
- 元组数据值可以访问，不能修改， 不能修改
- 元组数据可以是任意类型
- 总之，list所有特性，除了可修改外，元组都具有
- 也就意味着，list具有的一些操作，v比如索引，分片，序列相加，相乘，成员资格操作等，一模一样
'''
# 索引操作
t = (1,2,3,4,5)
print(t[3])
# incex: 求指定元素在元组中的位置
print(t.index(4))

# 超标错误
# print(t[6]) #此处会提示超标错误

t1 = t[1::2]
print(id(t))
print(id(t1))
print(t1)

# 切片可以超标
t2 = t[2:100]
print(t2)

# 序列相加
t1 = (1,2,3)
t2 = (4,5,6)
print(t1)
print(id(t1))
t1 += t2  #传址操作
print(t1)
print(id(t1))

# 以上操作类似于
t1 = (1,2,3)
t1 = (2,3,4)

# tuple的不可以修改，是指内容不可修改
# 修改tuple内容会导致报错

# 元组相乘
t = (1,2,3)
t = t *3
print(t)

# 元组的检测
t = (1,2,3)
if 2 in t:
  print("yes")
else:
  print("no")

# 元组的遍历，一般采用for
# 单程元组遍历
t = (1,2,3,'hello', 'i', 'love')
for i in t:
  print(i)

# 双层元组的遍历
t = ((1,2,3), (2,3,4), ("i", "love","china"))
# 对以上元组进行遍历
# 遍历方法1
for i in t:
  print(i)
# 遍历方法2
for k,m,n in t:
  print(k, "----", m, "-----", n)

# 元组变量交换法
# 两个变量交换值
a = 1
b = 3
print(a)
print(b)
print("*"*20)
a,b = b, a
print(a)
print(b)
##################################################################################
'''
集合-set
- 集合是高中数学中的一个概念
- 一堆确定的无序的唯一的数据，集合中每一个数据成为一个元素
'''
# 集合的含义
s = set()
print(type(s))
print(s)
print("*"*20)
# 此时，大括号内一定要有值，否则定义出的是一个dict字典
s = {1,2,3,4,5,6}
print(type(s))
print(s)

'''
集合的特点
- 集合内数据无序 ，即无法使用索引和分片
- 集合内数据元素具有唯一性，可以用来排除生蚝是数据
- 集合内的数据，str, int, float, tuple, 冰冻集合等，即内部只能旋转可哈希数据
'''
# 集合序列操作
# 成员检测 in, not in
s = {4, 5, 'i', 'lovw'}
print(s)
if 'i' in s:
  print('yes')

if 6 not in s:
  print('no')

# 集合的遍历操作
# for
s = {4, 5, 'i', 'lovw'}
for i in s:
  print(i)

# 带有元组的集合遍历
s = {(3, 4, 5), ('i', 'lovw',"asd"), (4,5,6)}
for k,m,n in s:
  print(k, "----", m, "---------", n)

for k in s:
  print(k)

# 集合的内涵
# 以下集合在初始化后启动过滤掉重复元素
s = {1,23,13,14,13,15}
print(s)

ss = {i for i in s}
print(ss)

# 带条件的集合内涵
sss = {i for i in s if i%2==0}
print(sss)

# 多循环的内层循环
s1 = {1,2,3,4}
s2 = {'i', 'a', 'asdf'}
s = {m*n for m in s2 for n in s1}
print(s)
print("*"*20)
s = {m*n for m in s2 for n in s1 if n==2}
print(s)

# 集合函数/关于集合的函数
# len, max, min：跟其它函数基本一致
s = {1,2,22,3,4,55,2}
print(len(s))
print(max(s))
print(min(s))

# sete:生成一个集合
l = [1,2,3,4,1,1,2,3,4]
s = set(l)
print(s)

# add:向集合内添加元素
s = {1}
s.add(334)
print(s)

# clear:原地清空数据
s = {12,34}
print(id(s))
s.clear()
print(id(s))

# copy: 拷贝
# remove： 删除指定值，直接改变原有值，报错
# discard:移除指定集合中指定的值， 不报错
s = {23,2,4,5,6,12,3,}
s.remove(4)
print(s)
s.discard(1)
print(s)
print("*"*40)

# pop 随机移除一个元素
s = {1,2,3,4,5,6,7}
d = s.pop()
print(d)
print(s)

# 集合函数
# intersection: 交集
# difference:差集
# union:并集
# issubset: 检查一个集合是否为另一个子集
# issuperset:检查一个集合是否为另一个超集
s1 = {1,2,3,4,5}
s2 ={5,6,7,8}
s_1 = s1.intersection(s2)
print(s_1)

s_2 = s1.difference(s2)
print(s_2)

s_3 = s1.issubset(s2)
print(s_3)

# 集合数学操作
s1 = {1,2,3,4,5}
s2 ={5,6,7,8}

s_1 = s1 - s2
print(s_1)

# frozen set:冰冻集合
# 冰冻和就是不可以进行任何修改的集合
# 是一种特殊的集合
s = frozenset()
print(type(s))
print(s)
print("*"*50)
###############################################################################
'''
dict 字典
- 字典是一种组合数据，没有顺序的组合数据，数据以建值对形式出现
'''
# 字典的创建
# 创建空字典
d = {}
print(d)
# 创建空字典
d = dict()
print(d)
# 创建带值的字典，每一组数据用冒号w隔开，每一对键值用逗号隔开
d = {"one":1, "two":2, "three":3}
print(d)

d = dict({"one":1, "two":2, "three":3})
print(d)

d = dict(one=1, two=2, three=3)
print(d)

d = dict([("one",1), ("two",2), ("three",3)])
print(d)
print("*"*50)

# 字典特征
# - 字典是序列类型，但是是无序序列，没有分片和索引
# - 字典中的数据每个都有键值对组成，即kv对
#   - key: 必须是可哈希的值， 比如： int, string,float,tuple，但 list,set,dict 不行
#   - value:任何值

# 字典常见操作
# 访问数据
d = {"one":1, "two":2, "three":3}
print(d["one"])

d["one"] = "eins"
print(d)

# 删除操作   del
del d["one"]
print(d)

# 成员检测 in, not in
d = {"one":1, "two":2, "three":3}
if 2 in d:
  print("value")

if "one" in d:
  print("key")

if ("tow",2) in d:
  print("kv")

# 遍历 在2和3区别大，代码不通用
# 按key来使用for循环
d = {"one":1, "two":2, "three":3}
for k in d:
  print(k, d[k])
# 以上可以如下操作
for k in d.keys():
  print(k, d[k])

# 只访问值
for v in d.values():
  print(v)

# 特殊用法
for k,v in d.items():
  print(k, "----", v)

# 字典生成式
dd = {k:v for k,v in d.items()}
print(dd)

# 加限制条件的字典生成
dd = {k:v for k,v in d.items() if v%2 == 0}
print(dd)

# 字典相关函数
# - 通用函数
#   - len, max, min, dict
#   - *str(字典)：返回字典的字符串格式
d = {"one":1, "two":2, "three":3}
print(str(d))

# clear：
# items:返回旁边骂人键值对组成的元组格式
# 
d = {"one":1, "two":2, "three":3}
i = d.items()
print(type(i))
print(i)

# keys: 返回字典的键组成的一个结构
k = d.keys()
print(type(k))
print(k)

# values:
v = d.values()
print(type(v))
print(v)

# get: 根据指定键返回相应值,好处是可以设置默认值
d = {"one":1, "two":2, "three":3}
print(d.get("on333"))
# get默认值是None，可以设置
print(d.get("one", 100))
print(d.get("one333", 100))

# fromkeys: 使用指定的序列作为键，使用一个值作为字典的e所有的键的值
l = ["eins", "zwei", "dree"]
# 注意fromkeys两个参数的类型
# 注意fromkeysy的调用主体
d = dict.fromkeys(l, "hahaha")
print(d)
