#

'''
- http://www.dabeaz.com/python/UnderstandingGIL.pdf
多线程 VS 多进程
- 程序： 一堆代码以文本形式存入一个文档
- 进程： 程序运行的一个状态
  - 包含地址空间、内存、数据栈等
  - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
- 线程
  - 一个进程的独立运行片段，一个进程可以由多个线程
  - 轻量化的进程
  - 一个进程的多个线程间共享数据和上下文运行环境
  - 互斥问题
- 全局解释器锁(GIL)
  - Python代码执行是由python虚拟机进行控制
  - 在主循环中更有一个控制线程在执行
- Python包
  - thread: 有问题不好用，python3改成了_thread
  - threading:通用的包
  - 案例 1 和 案例 2
- threading 的使用
  - 直接利用threading.Thread生成Thread实例
    - t = threading.Thread(target=xxx, args=(xxx,)) # target=函数名，args=参数
    - t.start(): 启动多线程
    - t.join(): 等待多线程执行完成
    - 案例 4
    - 案例 5 ，加入join
  - 守护线程- daemon
    - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束时结束
    - 一般认为，守护线程中不要或者不允许离开主线程独立运行
    - 守护线程案例能否有效果跟环境有关
    - 案例 6 非守护
    - 案例7  守护
  - 线程常用属性
    - threading.currentThread:
    - threading.enumerate: 返回一个包含正在运行线程的list
    - threading.activeCount
    - threading.setName
    - threading.getName
    - 案例 8
- 直接继承自threading.Thread
  - 直接继承Thread
  - 重写run函数
  - 类实例可以直接运行
  - 案例 9
  - 案例 10 
- 共享变量
  - 共享变量： 当多个线程同时访问一个变量时，会产生共享变量y问题
  - 案例 11
  - 解决方法： 锁、信号灯
  - 锁(Lock):
    - 是一个标准，表示一个线程在占用一些资源
    - 使用方法
      - 上锁
      - 使用共享资源
      - 取消锁，释放锁
    - 案例 12
    - 锁谁：哪个资料需要多个线程共享就锁谁
    - 理解锁： 锁其实不是锁谁，而是一个令牌
  - 线程安全问题
    - 如果一个资源/变量，对于多线程，不用加锁也不会引起任何问题，则称为线程安全
    - 线程不安全变量类型： list, set, dict
    - 线程安全变量类型：queue
  - 生产者消费者问题
    - 一个模型:可以用来搭建消息队列
    - queue 是一个用来存放变量的数据结构，特点是先进先出，内部元素排除，可以理解成一个特殊的list
    - 案例 13
  - 死锁问题
    - 案例 14
  - 锁的等待时间问题
    - 案例 15
  - semaphore -- threading.semaphore
    - 允许一个资源最多由几个多线程同时使用
    - 案例 16
  - threading.Timer
    - Timer是利用多线程，在指定时间后启动一个功能
    - 案例 17
  - 可重入锁 - threading.RLock
    - 一个锁，可以被一个线程多次申请
    - 主要解决递归调用的时候，需要申请锁的情况
    - 案例 18

线程替代方案
- subprocess
  - 完全跳过线程，使用进程
  - 是派生进程的主要替代方案
  - python2.4后引入
- multiprocessing
  - 使用threading接口派生，使用了子进程
  - 允许为多核或多CPU派生进程，接口跟threading非常相似
  - python2.6后引入
- concurrent.futures
  - 新的异步执行模块
  - 任务级别的操作
  - python3.2后引入

多进程
- 进程间通讯(InterprocessCommunication, IPC)
- 进程之间无任何共享状态
- 进程的创建
  - 直接生成Process实例对象 案例 19
  - 派生子类   案例 10
- 在 os 中查看 pid ppid以及他们的关系
  - 案例 21
- 生产者消费模型
  - JoinableQueue: 
  - 案例 22
  - 队列中哨兵的使用，案例 23
  - 哨兵改进，案例 24
'''
# 案例 1
import time
import _thread as thread
# def loop1():
#   print("start loop 1 at :", time.ctime())
#   time.sleep(1)
#   print("end loop 1 at:",time.ctime())

# def loop2():
#   print("start loop 2 at :", time.ctime())
#   time.sleep(2)
#   print("end loop 2 at:",time.ctime())

# def main():
#   print("start at :", time.ctime())
#   # loop1()
#   # loop2()
#   thread.start_new_thread(loop1, ())
#   thread.start_new_thread(loop2, ())
#   print("end at:",time.ctime())

# if __name__ == '__main__':
#   main()
#   while True:
#     time.sleep(5)

# 案例 2
# def loop1(in1):
#   print("start loop 1 at :", time.ctime())
#   print("loop 1 ", in1)
#   time.sleep(1)
#   print("end loop 1 at:",time.ctime())

# def loop2(in1, in2):
#   print("start loop 2 at :", time.ctime())
#   print("loop 2 ", (int1, in2))
#   time.sleep(2)
#   print("end loop 2 at:",time.ctime())

# def main():
#   print("start at :", time.ctime())
#   # loop1()
#   # loop2()
#   thread.start_new_thread(loop1, ("wangdana",))
#   thread.start_new_thread(loop2, ("lili", "lucy"))
#   print("end at:",time.ctime())

# if __name__ == '__main__':
#   main()
#   while True:
#     time.sleep(5)

# 案例 4
#import time
import threading
# def loop1(in1):
#   print("start loop 1 at :", time.ctime())
#   print("loop 1 ", in1)
#   time.sleep(1)
#   print("end loop 1 at:",time.ctime())

# def loop2(in1, in2):
#   print("start loop 2 at :", time.ctime())
#   print("loop 2 ", (in1, in2))
#   time.sleep(2)
#   print("end loop 2 at:",time.ctime())

# def main():
#   print("start at :", time.ctime())
#   # loop1()
#   # loop2()
#   t1 = threading.Thread(target=loop1, args=("wangdana",))
#   t1.start()
#   t2 = threading.Thread(target=loop2, args=("lili", "lucy"))
#   t2.start()
#   print("end at:",time.ctime())

# if __name__ == '__main__':
#   main()
#   while True:
#     time.sleep(5)
#     break

# 案例 5
# def loop1(in1):
#   print("start loop 1 at :", time.ctime())
#   print("loop 1 ", in1)
#   time.sleep(1)
#   print("end loop 1 at:",time.ctime())

# def loop2(in1, in2):
#   print("start loop 2 at :", time.ctime())
#   print("loop 2 ", (in1, in2))
#   time.sleep(2)
#   print("end loop 2 at:",time.ctime())

# def main():
#   print("start at :", time.ctime())
#   # loop1()
#   # loop2()
#   t1 = threading.Thread(target=loop1, args=("wangdana",))
#   t1.start()
#   t2 = threading.Thread(target=loop2, args=("lili", "lucy"))
#   t2.start()
#   t1.join()
#   t2.join()
#   print("end at:",time.ctime())

# if __name__ == '__main__':
#   main()

# 案例 6
# def fun():
#   print("fun start ...")
#   time.sleep(2)
#   print("fun end ...")

# print("main thread start")
# t1 = threading.Thread(target=fun, args=())
# t1.start()

# time.sleep(1)
# print("main thread end")

# 案例 7
# def fun():
#   print("fun start ...")
#   time.sleep(2)
#   print("fun end ...")

# print("main thread start")
# t1 = threading.Thread(target=fun, args=())
# t1.setDaemon(True)
# # t1.Daemon= True
# t1.start()

# time.sleep(1)
# print("main thread end")

# 案例 8
# def loop1():
#   print("start loop 1 at :", time.ctime())
#   time.sleep(6)
#   print("end loop 1 at:",time.ctime())

# def loop2():
#   print("start loop 2 at :", time.ctime())
#   time.sleep(1)
#   print("end loop 2 at:",time.ctime())

# def loop3():
#   print("start loop 3 at :", time.ctime())
#   time.sleep(5)
#   print("end loop 3 at:",time.ctime())

# def main():
#   print("start at :", time.ctime())
#   # loop1()
#   # loop2()
#   t1 = threading.Thread(target=loop1, args=())
#   t1.setName("THR-1")
#   t1.start()
#   t2 = threading.Thread(target=loop2, args=())
#   t2.setName("THR-2")
#   t2.start()
#   t3 = threading.Thread(target=loop3, args=())
#   t3.setName("THR-3")
#   t3.start()

#   time.sleep(3)
#   for thr in threading.enumerate():
#     print("正在运行线程的名字是 {0}".format(thr.getName()))

#   print("正在运行线程的数量为：{0}".format(threading.activeCount()))
#   print("end at:",time.ctime())
  
# if __name__ == '__main__':
#   main()
#   while True:
#     time.sleep(6)
#     break

# 案例 9
# class MyThread(threading.Thread):
#   def __init__(self, arg):
#     super(MyThread, self).__init__()
#     self.arg = arg
  
#   def run(self):
#     time.sleep(2)
#     print("The args for this class is {0}".format(self.arg))

# for i in range(5):
#   t = MyThread(i)
#   t.start()
#   t.join()
# print("Main thread is done !!!!!!")

# 案例 10
# loop = [4,2]
# class ThreadFunc:
#   def __init__(self, name):
#     self.name = name
  
#   def loop(self, nloop, nsec):
#     print("start loop", nloop, "at ", time.ctime())
#     time.sleep(nsec)
#     print("Done loop", nloop, "at ", time.ctime())
  
# def main():
#   print("start at: ", time.ctime())

#   t = ThreadFunc("loop")
#   t1 = threading.Thread(target=t.loop, args=("LOOP1", 4))
#   t2 = threading.Thread(target=ThreadFunc("loop").loop, args=("LOOP2",2))

#   t1.start()
#   t2.start()

#   t1.join()
#   t2.join()
#   print("ALL done at: ", time.ctime())

# if __name__ == '__main__':
#   main()

# 案例 11
# sum = 0
# loopsum = 100000

# def myAdd():
#   global sum, loopsum
#   for i in range(1, loopsum):
#     sum += 1

# def myMinu():
#   global sum, loopsum
#   for i in range(1, loopsum):
#     sum -= 1

# if __name__ == '__main__':
#   # myAdd()
#   # print(sum)
#   # myMinu()
#   # print(sum)

#   print("start ... {0}".format(sum))
#   t1 = threading.Thread(target=myAdd, args=())
#   t2 = threading.Thread(target=myMinu, args=())
#   t1.start()
#   t2.start()
#   t1.join()
#   t2.join()
#   print("endi ... {0}".format(sum))

# 案例 12
# sum = 0
# loopsum = 100000
# lock = threading.Lock()

# def myAdd():
#   global sum, loopsum
#   for i in range(1, loopsum):
#     # 上锁
#     lock.acquire()
#     sum += 1
#     # 释放锁
#     lock.release()

# def myMinu():
#   global sum, loopsum
#   for i in range(1, loopsum):
#     # 上锁
#     lock.acquire()
#     sum -= 1
#     # 释放锁
#     lock.release()

# if __name__ == '__main__':
#   # myAdd()
#   # print(sum)
#   # myMinu()
#   # print(sum)

#   print("start ... {0}".format(sum))
#   t1 = threading.Thread(target=myAdd, args=())
#   t2 = threading.Thread(target=myMinu, args=())
#   t1.start()
#   t2.start()
#   t1.join()
#   t2.join()
#   print("endi ... {0}".format(sum))

# 案例 13
# Python 2.x 的用法 from Queue import Queue
# Python 3.x 的用法 import Queue
import queue

# class Producer(threading.Thread):
#   def run(self):
#     global queue
#     count = 0
#     while True:
#       # qsize 返回 queue 内容长度
#       if queue.qsize() < 1000:
#         for i in range(100):
#           count += 1
#           msg = "生成产品" + str(count)
#           # put 往 queue 放入一个值
#           queue.put(msg)
#           print(msg)
#       time.sleep(0.5)


# class Consumer(threading.Thread):
#   def run(self):
#     global queue
#     while True:
#       # qsize 返回 queue 内容长度
#       if queue.qsize() > 100:
#         for i in range(100):
#           # get 从 queu 里面拿出一个值
#           msg = self.name + " 消费了 " +queue.get()          
#           print(msg)
#       time.sleep(1)

# if __name__ == '__main__':
#   queue = queue.Queue()

#   for i in range(500):
#     queue.put("初始产品"+str(i))
#   for i in range(2):
#     p = Producer()
#     p.start()
#   for i in range(5):
#     c = Consumer()
#     c.start()

# 案例 14
# lock1 = threading.Lock()
# lock2 = threading.Lock()

# def func_1():
#   print("func_1 starting .......")
#   lock1.acquire()
#   print("func_1 申请了 lock1 ...")
#   time.sleep(2)
#   print("func_1 等待 lock2 ....")
#   lock2.acquire()
#   print("func_1 申请了 lock2 ...")
#   lockk2.release()
#   print("func_1 释放了 lock2")
#   lock1.release()
#   print("func_1 释放了 lock1")

#   print("func_1 done ....")

# def func_2():
#   print("func_2 starting .......")
#   lock2.acquire()
#   print("func_2 申请了 lock2 ...")
#   time.sleep(2)
#   print("func_2 等待 lock1 ....")
#   lock1.acquire()
#   print("func_2 申请了 lock1 ...")
#   lockk1.release()
#   print("func_2 释放了 lock1")
#   lock2.release()
#   print("func_2 释放了 lock2")

#   print("func_2 done ....")
  
# if __name__ == '__main__':
#   print("start ... {0}".format(sum))
#   t1 = threading.Thread(target=func_1, args=())
#   t2 = threading.Thread(target=func_2, args=())
#   t1.start()
#   t2.start()
#   t1.join()
#   t2.join()
#   print("endi ... {0}".format(sum))


# 案例 15
# lock1 = threading.Lock()
# lock2 = threading.Lock()

# def func_1():
#   print("func_1 starting .......")
#   rst1 = lock1.acquire(timeout=1)
#   print("func_1 申请了 lock1 ...")
#   time.sleep(2)
#   print("func_1 等待 lock2 ....")
  
#   rst = lock2.acquire(timeout=2)
#   if rst:
#     print("func_1 申请了 lock2 ...")
#     lockk2.release()
#     print("func_1 释放了 lock2")
#   else:
#     print("func_1 没申请到 lock2")

#   if rst1:
#     lock1.release()
#   print("func_1 释放了 lock1")

#   print("func_1 done ....")

# def func_2():
#   print("func_2 starting .......")
#   lock2.acquire()
#   print("func_2 申请了 lock2 ...")
#   time.sleep(2)
#   print("func_2 等待 lock1 ....")
#   lock1.acquire()
#   print("func_2 申请了 lock1 ...")
#   lock1.release()
#   print("func_2 释放了 lock1")
#   lock2.release()
#   print("func_2 释放了 lock2")

#   print("func_2 done ....")
  
# if __name__ == '__main__':
#   print("start ... {0}".format(sum))
#   t1 = threading.Thread(target=func_1, args=())
#   t2 = threading.Thread(target=func_2, args=())
#   t1.start()
#   t2.start()
#   t1.join()
#   t2.join()
#   print("endi ... {0}".format(sum))

# 案例 16
# semaphore = threading.Semaphore(3)

# def func():
#   if semaphore.acquire():
#     for i in range(5):
#       print(threading.currentThread().getName() + 'get semaphore')
#     time.sleep(15)
#     print(threading.currentThread().getName() + ' release semaphore')
#     semaphore.release()

# for i in range(8):
#   t1 = threading.Thread(target=func)
#   t1.start()

# 案例 17
# def func():
#   print("starting ....")
#   time.sleep(4)
#   print("ending....")

# if __name__ == '__main__':
#   t = threading.Timer(6, func)
#   t.start()
  
#   i = 0
#   while True:
#     print("{0} .......".format(i))
#     time.sleep(3)
#     i += 1

# 案例 18
# class MyThread(threading.Thread):
#   def run(self):
#     global num
#     time.sleep(1)

#     if mutex.acquire(1):
#       num += 1
#       msg = self.name + "set num to " + str(num)
#       print(msg)
#       mutex.acquire()
#       mutex.release()
#       mutex.release()

# num = 0
# # mutex = threading.Lock()
# mutex = threading.RLock() # 可重入锁

# def testTh():
#   for i in range(5):
#     t = MyThread()
#     t.start()

# if __name__ == '__main__':
#   testTh()

# 案例 19
import multiprocessing

# def clock(interval):
#   while True:
#     print("the time is %s" % time.ctime())
#     time.sleep(interval)

# if __name__ == '__main__':
#   p = multiprocessing.Process(target=clock, args=(5,))
#   p.start()

# 案例 20
# class ClockProcess(multiprocessing.Process):
#   # init 构造函数、 run 函数； 两个重要函数
#   def __init__(self, interval):
#     super().__init__()
#     self.interval = interval

#   def run(self):
#     while True:
#       print("the time is %s" % time.ctime())
#       time.sleep(self.interval)

# if __name__ == '__main__':
#   p = ClockProcess(3)
#   p.start()

# 案例 21
import os

# def info(title):
#   print(title)
#   print("module name:", __name__)
#   # 父进程ID
#   print("parent process:", os.getppid())
#   # 子进程ID
#   print("process id:", os.getpid())

# def f(name):
#   info("function f")
#   print("hello", name)

# if __name__ == '__main__':
#   info("main line")
#   p = multiprocessing.Process(target=f, args=('bob',))
#   p.start()
#   p.join()

# 案例 22
# def consumer(input_q):
#   print("Into consumer:", time.ctime())
#   while True:
#     item = input_q.get()
#     print("pull ", item, " out of 1")
#     input_q.task_done()
#   print("out of consumer:", time.ctime())

# def producer(sequence, output_q):
#   print("into producer:", time.ctime())
#   for item in sequence:
#     output_q.put(item)
#     print("put ", item, " into q")
#   print("out producer:", time.ctime())

# if __name__ == '__main__':
#   q = multiprocessing.JoinableQueue()

#   cons_p = multiprocessing.Process(target=consumer, args=(q,))
#   cons_p.daemon = True
#   cons_p.start()

#   sequence = [1,2,3,4]
#   producer(sequence, q)
#   # 等待所有项被处理
#   q.join()

# 案例 23
# def consumer(input_q):
#   print("Into consumer:", time.ctime())
#   while True:
#     item = input_q.get()
#     if item is None:
#       break
#     print("pull ", item, " out of 1")
#   print("out of consumer:", time.ctime())

# def producer(sequence, output_q):
#   print("into producer:", time.ctime())
#   for item in sequence:
#     output_q.put(item)
#     print("put ", item, " into q")
#   print("out producer:", time.ctime())

# if __name__ == '__main__':
#   q = multiprocessing.Queue()

#   cons_p = multiprocessing.Process(target=consumer, args=(q,))
#   cons_p.daemon = True
#   cons_p.start()

#   sequence = [1,2,3,4]
#   producer(sequence, q)
#   q.put(None)
#   # 等待所有项被处理
#   cons_p.join()

  
# 案例 24
def consumer(input_q):
  print("Into consumer:", time.ctime())
  while True:
    item = input_q.get()
    if item is None:
      break
    print("pull ", item, " out of 1")
  print("out of consumer:", time.ctime())

def producer(sequence, output_q):
  print("into producer:", time.ctime())
  for item in sequence:
    output_q.put(item)
    print("put ", item, " into q")
  print("out producer:", time.ctime())

if __name__ == '__main__':
  q = multiprocessing.Queue()
  
  cons_p1 = multiprocessing.Process(target=consumer, args=(q,))
  cons_p1.start()
  cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
  cons_p2.start()

  sequence = [1,2,3,4]
  producer(sequence, q)
  q.put(None)
  q.put(None)
  # 等待所有项被处理
  cons_p1.join()
  cons_p2.join()