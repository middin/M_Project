#

'''
LOG
- 日志
  - 日志的级别, 从低到高
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
  - IO操作 ==> 不要频繁操作
  - LOG作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
  - 日志信息
    - time
    - 地点
    - level
    - 内容
  - 成熟的第三方日志
    - log4j
    - log4php
    - logging

logging模块
- 日志级别
  - 级别可自定义
  - DEBUG
  - INFO
  - ERROR
  - CRITICAL
- 初始化/写日志实例需要指定级别，只有当级别等于或者高于指定级别才被记录
- 使用方式
  - 直接使用 logging(封装了其他组件)
  - logging 的四大组件
# logging 模块级别的日志
- 使用以下几个函数
  - logging.debug(msg, *args, **kwargs)
  - logging.info(msg, *args, **kwargs)
  - logging.warning(msg, *args, **kwargs)
  - logging.error(msg, *args, **kwargs)
  - logging.critical(msg, *args, **kwargs)
  - logging.log(level, *args, **kwargs)
  - logging.basicConfig(**kwargs)
    - 只在第一次调用时起作用
    - 不配置logger则使用默认值
      - 输出：sys.stderr
      - 级别：WARNING
      - 格式：level:log_name:content
- format 参数
    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息

asctime %(asctime)s  日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
created %(created)f  日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
relativeCreated %(relativeCreated)d 日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
msecs   %(msecs)d   日志事件发生事件的毫秒部分
levelname   %(levelname)s   该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
levelno %(levelno)s 该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
name    %(name)s    所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
message %(message)s 日志记录的文本内容，通过 msg % args计算得到的
pathname    %(pathname)s    调用日志记录函数的源码文件的全路径
filename    %(filename)s    pathname的文件名部分，包含文件后缀
module  %(module)s  filename的名称部分，不包含后缀
lineno  %(lineno)d  调用日志记录函数的源代码所在的行号
funcName    %(funcName)s    调用日志记录函数的函数名
process %(process)d 进程ID
processName %(processName)s 进程名称，Python 3.1新增
thread  %(thread)d  线程ID
threadName  %(thread)s  线程名称
- 案例 1

logging萨芬内容处理流程
- 四大组件
  - 日志器(Logger): 产生日志的一个接口
    - 产生一个日志
    - 操作
      - Logger.setLevel()
      - Logger.addHandler() 和 Logger.removeHandler()
      - Logger.addFilter() 和 Logger.removeFilter()
      - Logger.debug()
      - Logger.exception():
      - Logger.log()
    - 如何得到一个logger对象
      - 实例化
      - logging.getLogger()
  - 处理器(Handler): 把产生的日志发送到相应的目的地
    - 把 log 发送到指定位置
    - 方法
      - setLevel
      - setFormat
      - addFilter, removeFilter
    - 不需要直接使用，Handler是基类
      - logging.StreamHandler
      - logging.FileHandler
      - logging.handler.RotatingFileHandler
      - logging.handler.TimedRotatingFileHandler
      - logging.handler.HTTPHandler
      - logging.handler.SMTPHandler
      - logging.NullHanlder
    - format 类
      - 直接实例化
      - 可以继续 Format 添加特殊内容
      - 三个参数
        - fmt:
        - datefmt:
        - style
    - filter 类
      - 可以被 Handler和Logger使用
      - 控制传递过来的信息的具体内容
    - 案例 2
  - 过滤器(Filter): 更精细的控制日志输出
  - 格式器(Formatter): 对输出的信息进行格式化

'''
color = ['read', 'green', 'yellow', 'blue']
for green in color:
  if green == 'green':
    print("Green")

import logging
# 案例 1
# 参考   https://www.cnblogs.com/yyds/p/6901864.html
LOG_FORMAT = "%(asctime)s===========%(levelname)8s++++++++%(message)s"
logging.basicConfig(filename="logging.log", level=logging.DEBUG, format=LOG_FORMAT)

# 以下写文件后，将不会在窗口输出日志信息
#logging.basicConfig(filename="logging.log", level=logging.DEBUG)

#logging.basicConfig(level=logging.DEBUG)

logging.debug("debug log")
logging.info("info log")
logging.warning("warning log")
logging.error("error log")
logging.critical("critical log")

# 另一种方式
logging.log(logging.DEBUG, "debug log")
logging.log(logging.INFO,"info log")
logging.log(logging.WARNING,"warning log")
logging.log(logging.ERROR,"error log")
logging.log(logging.CRITICAL,"critical log")

# 案例 2
import logging
import logging.handlers
import datetime

# 定义logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
#rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)%s)"))

f_handler = logging.FileHandler("error.log")
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)%s[:%(lineno)d] - %(message)%s)"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug("debug log")
logger.info("info log")
logger.warning("warning log")
logger.error("error log")
logger.critical("critical log")