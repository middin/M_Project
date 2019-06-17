# 

'''
协程
- 参考资料
  - http://python.jobbole.com/86481/
  - http://python.jobbole.com/87310/

迭代器
- 可迭代(Iterable):直接作用于for循环的变量
- 迭代器(Iterator):不但可以作用于for循环，还可以被 nwxt 调用
- list是典型的可迭代对象，但不是迭代器
- 通过 isinstance 判断
- iterable 和 iterator 可以转换
  - 通过 iter 函数
'''
# 可迭代
l = [i for i in range(10)]

# l 是可迭代的，但不是迭代器
for idx in l:
  # print(idx)
  pass

# range 是个迭代器
for i in range(5):
  # print(i)
  pass

# isinstance 案例
# 判断是否可迭代
from collections import Iterable, Iterator

print(isinstance(l, Iterable))
print(isinstance(l, Iterator))

# iter 函数
s = "I love chian"
print(isinstance(s, Iterable))
print(isinstance(s, Iterator))

s_iter = iter(s)
print(isinstance(s_iter, Iterable))
print(isinstance(s_iter, Iterator))

'''
生成器
- generator: 一边循环一边计算下一个元素的机制/算法
- 需要满足三个条件：
  - 每次调用都生产出for循环需要的下一个元素或者
  - 如果达到最后一个后，爆出StopIteration异常
  - 可以被 next 函数调用
- 如何生成一个生成器
  - 直接使用
  - 如果函数中包含 yield , 则这个函数就叫生成器
  - next 调用函数， 遇到 yield 返回
'''
# 直接使用生成器
l = [ x*x for x in range(5)] # 列表生成器
g = ( x*x for x in range(5)) # 生成器
print(type(l))
print(type(g))
print(isinstance(g, Iterator))

# 函数案例
# 生成器的b案例
def odd():
  print("Step 1")
  yield 1
  print("Step 2")
  yield 2
  print("Step 3")
  yield 3

g = odd()
one = next(g)
print(one)
two = next(g)
print(two)

# for 循环调用生成器
def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    print(b)
    a, b = b, a+b
    n += 1

  return "None"

fib(5)
print("*"*50)

# 斐波那契数列的生成器写法

def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a+b
    n += 1

  return 'None'

g = fib(5)
for i in range(5):
  rst = next(g)
  print(rst)
print("*"*50)

g = fib(10)  
for i in g:
  print(i)
print("*"*50)

'''
协程
- 历史历程
  - 3.4 引入协程，用yield实现
  - 3.5 引入协程语法
  - 实现协程比较好的包有asyncio, tornado, vevent
- 定义：协程是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或者开始执行程序
- 从技术角度讲，协程就是一个可以暂停执行的函数，或者干脆把协程理解成生成器
- 协程实现
  - yield 返回
  - send 调用
- 协程的四个状态
  1. GEN_CREATED：等待开始执行 
  2. GEN_RUNNING：解释器正在执行 
  3. GEN_SUSPENED：在yield表达式处暂停 
  4. GEN_CLOSED：执行结束
  - next 预计(prime)
  - 代码案例2
  - 最先调用 next(sc) 函数这一步通常称为“预激”（prime）协程==（即，让协程向前执行到第一个 yield 表达式，准备好作为活跃的协程使用）
- 协程终止
  - 协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象)
  - 终止协程的一种方式：发送某个哨符值，让协程退出 ，内置的None 和 Ellipsis 等常量经常用途哨符值==
- yield from
  - 调用协程为了得到返回值，协程必须正常终止
  - 生成器正常终止会发出 StopIteration 异常，异常对象的value属性保存返回值 
  - yield from 从内部捕获 StopIteration 异常
  - 案例 3
  - 委派生成器
    - 包含 yield from 表达式的生成器函数
    - 委派生成器在 yield from 表达式出暂停，调用方可以把直接把数据发给自生成器
    - 子生成器在把产出的值发给调用方
    - 子生成器在最后，解释器会抛出 StopIteration, 并且把返回值附加到异常对象
    - 案例 4
'''
# 协程代码案例 1
def simple_coroutine():
  print("-> start")
  x = yield
  print("-> revieved", x)

sc = simple_coroutine()
print(1111)
# 可以使用sc.send(None)， 效果一样
next(sc) # 预计
print(2222)
try:
  sc.send("zhexiao")
except Exception as e:
  print(e)

print("*"*50)

# 协程的状态   案例 2
def simple_coroutine(a):
  print("-> start")
  b = yield a
  print("-> revieved", a, b)
  c = yield a+b
  print("-> revieved", a, b, c)
  yield a+b+c

sc = simple_coroutine(5)

aa = next(sc)
print(aa)
bb = sc.send(6)
print(bb)
cc = sc.send(7)
print(cc)
print("*"*50)

# 协程的状态   案例 3
def gen():
  for c in 'AB':
    yield c

print(list(gen()))

def gen_new():
  yield from 'AB'

print(list(gen_new()))
print("*"*50)

# 案例 4  委派生成器
from collections import namedtuple

ResClass = namedtuple("res", "count average term")

# 子生成器
def average():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return ResClass(count, average, term)

# 委派生成器
def grouper(storages, key):
    while True:
        storages[key] = yield from average()
        print("test...", storages[key])

# 客户端代码
def client():
    process_data = {
        'boys_2':[39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        "boys_1":[1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
    }

    storages = {}
    for k,v in process_data.items():
        # 获取协程
        coroutine = grouper(storages, k)

        # 预激协程
        next(coroutine)

        # 发送数据到协程
        for dt in v:
            coroutine.send(dt)
        
        # 终止协程
        coroutine.send(None)
    print(storages)

# run
client()
print("*"*50)

'''
剩下的内容
- xml,json
- re, xpath
- 网络编程: socket(TCP/IP UDP), ftp, mail
- http 协议 ==> http web server 小项目
- django
'''

# asyncio
# - python3.4开始引入标准库中，内置对异常IO的支持
# - asyncio 本身是一个消息循环
# - 步骤：
#   - 创建消息循环
#   - 把协程导入
#   - 关闭
# 案例
import threading
import asyncio

# 使用协程
@asyncio.coroutine
def hello():
    print('hello (%s)' % threading.currentThread())
    print('start ...(%s)' % threading.currentThread())
    yield from asyncio.sleep(10)
    print('Done...(%s)' % threading.currentThread())
    print('hello again...(%s)' % threading.currentThread())

# 启动消息循环
loop = asyncio.get_event_loop()
# 定义任务
tasks = [hello(), hello()]
# asyncio 使用 wait 等待 task 执行
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 案例
@asyncio.coroutine
def wget(host):
    print("wget %s..."% host)
    # 异步请求网络地址
    connect = asyncio.open_connection(host, 88)
    # 注意 yield from 的用法
    read, write = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %\r\n\r\n' % host
    writer.write(header.encode('uft-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readLine()
        # http 协议的换行使用\r\n
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.bbaid.com', 'www.sina.cn']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''
async and await
- 为了更好的表示异步IO
- PYTHON3.5引入 
- 让协程代码更简洁
- 使用上，可以简单的进行替换
    - 用 async 替换 @asyncio.coroutine
    - await 替换　yield from

aiohttp
- asyncio 实现单线程的并发io, 在客户端用处不大
- 在服务器端可以 asyncio + coroutine 配合，因为http是io操作
- asyncio 实现了 tcp, udp, ssl 等协议
- aiohttp 是给予 asyncio 实现的 http 框架
- pip install aiohttp 安装
'''
# 案例
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.endoce('uft-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

# concurrent.futures
# - python3 新增的库
# - 类似其它语言的线程池的概念
# - 利用multiprocessing 实现真正并行计算
# - 核心原理：
#   - 以子进程形式，并行运行多个python解释器
#   - 从而令python程序可以利用多核CPU来提升执行速度
#   - 由于子进程与主解释器相分享，他r们的全局解释器锁也是相互独立的
#   - 每个子进程都能够完整的使用一个CPU内核
# - - concurrent.futures.Executor
    # - ThreadPoolExecutor
    # - ProcessPoolExecutor
    # - 执行时，需要自行选择
# - submit(fn, args, kwargs)
#   - fn 异步执行的函数
#   - args, kwargs 参数
# 案例
from concurrent.futures import ThreadPoolExecutor
import time

def return_future(msg):
    time.sleep(3)
    return msg

# 创建一个线程池
pool = ThreadPoolExecutor(max_workers=2)
# 往线程池加入2个task
f1 = pool.submit(return_future, 'hello')
f2 = pool.submit(return_future, 'world')

# 等待执行完毕
print(f1.done())
time.sleep(3)
print(f2.done())

# 结果
print(f1.result())
print(f2.result())

# current 中的 map 函数
# - map(fn, \*iterables, timeout=None)
#     - 跟 map 函数类似
#     - 函数需要异步执行
#     - timeout 超时时间
import time, re
import os, datetime
from concurrent import futures

data = ['1', '2']

def wait_on(argument):
    print(argument)
    time.sleep(2)
    return 'ok'

ex = futures.ThreadPoolExecutor(max_workers=2)
for i in ex.map(wait_on, data):
    print(i)

# future
# - 未来实现目前的事件

