#
'''
异常
- 广义上的错误分为错误和异常
- 错误指的是可以人为避免
- 异常是指在语法逻辑正确的前提下，出现的问题
- 在python里，异常是一个类，可以处理和使用
- 异常的分类
  BaseException 所有异常的基类
  SystemExit 解释器请求退出
  KeyboardInterrupt 用户中断执行(通常是输入^C)
  Exception 常规错误的基类
  StopIteration 迭代器没有更多的值
  GeneratorExit 生成器(generator)发生异常来通知退出
  StandardError 所有的内建标准异常的基类
  ArithmeticError 所有数值计算错误的基类
  FloatingPointError 浮点计算错误
  OverflowError 数值运算超出最大限制
  ZeroDivisionError 除(或取模)零 (所有数据类型)
  AssertionError 断言语句失败
  AttributeError 对象没有这个属性
  EOFError 没有内建输入,到达EOF 标记
  EnvironmentError 操作系统错误的基类
  IOError 输入/输出操作失败
  OSError 操作系统错误
  WindowsError 系统调用失败
  ImportError 导入模块/对象失败
  LookupError 无效数据查询的基类
  IndexError 序列中没有此索引(index)
  KeyError 映射中没有这个键
  MemoryError 内存溢出错误(对于Python 解释器不是致命的)
  NameError 未声明/初始化对象 (没有属性)
  UnboundLocalError 访问未初始化的本地变量
  ReferenceError 弱引用(Weak reference)试图访问已经垃圾回收了的对象
  RuntimeError 一般的运行时错误
  NotImplementedError 尚未实现的方法
  SyntaxError Python 语法错误
  IndentationError 缩进错误
  TabError Tab 和空格混用
  SystemError 一般的解释器系统错误
  TypeError 对类型无效的操作
  ValueError 传入无效的参数
  UnicodeError Unicode 相关的错误
  UnicodeDecodeError Unicode 解码时的错误
  UnicodeEncodeError Unicode 编码时错误
  UnicodeTranslateError Unicode 转换时错误
  Warning 警告的基类
  DeprecationWarning 关于被弃用的特征的警告
  FutureWarning 关于构造将来语义会有改变的警告
  OverflowWarning 旧的关于自动提升为长整型(long)的警告
  PendingDeprecationWarning 关于特性将会被废弃的警告
  RuntimeWarning 可疑的运行时行为(runtime behavior)的警告
  SyntaxWarning 可疑的语法的警告
  UserWarning 用户代码生成的警告 

异常处理
- 不能保证程序永远正确运行
- 但是，必须保证程序 在最坏的情况下得到的问题被妥善的处理
- python的异常处理模块全部语法为：
    try:
      尝试实现某个操作，
      如果没有出现异常，任务就可以完成
      如果出现异常，将异常从当前代码块扔出尝试解决异常
    except 异常类型1:
      解决方案2: 用于尝试在此处处理异常解决问题
    except 异常类型2:
      解决方案2: 用于尝试在此处处理异常解决问题
    except ():
      解决方案
    else:
      没出现异常，执行此处代码
    finally:
      无论有无异常，都要执行的代码
- 流程
  - 执行try下面的语句
  - 如果出现异常，则在except语句里面查找对应异常病进行处理
  - 如果没有异常，则执行else语句内容
  - 最后，不客是否出现异常，都要执行finally语句
- 除except（最少一个）以外，else和finally可靠
'''
# 简单异常处理
# 给出提示信息
try:
  num = int(input("plz input your num:"))
  rst = 100/num
  print("rst = {0}".format(rst))
# 捕获异常，把异常实例化，出错信息会在实例里
# 注意以下写法
except ZeroDivisionError as e:
  print("divisinn is not zero")
  print(e)
  # exit 程序彻底退出
  #exit()
except NameError as e:
  print(e)
except Exception as e:
  print(e)
print("*"*50)

# 用户手动引发异常
# - 当某些情况，用户希望自己引发一个异常时，可以使用raise 关键字来引发异常
# raise 案例 1
try:
  print("aaaaa")
  print(3.1415926)
  # 手动引发一个异常
  # 注意语法： raise ErrorClassName
  raise ValueError
  print("no over")
except NameError as e:
  print(e)
except ValueError as e:
  print("ValueError")
except Exception as e:
  print(e)
finally:
  print("exec ...")
print("*"*50)

# raise 案例 2
# 自己定义异常
# 需要注意： 自定义异常必须是系统异常的子类
class DanaError(ValueError):
  pass

try:
  print("aaaaa")
  print(3.1415926)
  # 手动引发一个异常
  # 注意语法： raise ErrorClassName
  raise DanaError
  print("no over")
except NameError as e:
  print(e)
#except DanaError as e:
#  print("DanaError")
except ValueError as e:
  print("ValueError")
except Exception as e:
  print(e)
finally:
  print("exec ...")
print("*"*50)

# else 语句案例
try:
  num = int(input("plz input your num:"))
  rst = 100/num
  print("rst = {0}".format(rst))
except Exception as e:
  print("Exception")
else:
  print("No Exception")
finally:
  print("执行...")
print("*"*50)

'''
关于自定义异常
- 只要是raise异常，则推荐自定义异常
- 在自定义异常时，一般包含以下内容：
    - 自定义发生异常的异常代码
    - 自定义发生异常后的问题提示
    - 自定义发生异常的行数
- 最终 的目的， 一旦发生异常，方便程序 员快速定位错误现场
'''
