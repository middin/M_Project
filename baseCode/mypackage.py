#
'''
1. 模块
- 一个模块就是一个包含python代码的文件。后续.py，模块就是h个python文件
- 模块的用途
  - 程序太大，编写维护不方便，需要拆分
  - 模块可以增加代码重复利用的方式
  - 当做w命名空间使用，避免命名冲突
- 如何定义模块
  - 模块就是一个普通文件，所以任何代码可以直接书写
  - 不过根据模块的规范，最好在模块中编写以下内容
    - 函数（单一功能）
    - 类（相似功能的组合，或者类似业务模块）
    - 测试代码
- 如何使用模块
  - 模块直接导入使用
    - 假如模块名称直接以数字开头，需要借助importlib帮助
  - 语法
        import module_name
        module_name.function_name
        module_name.class_name
  - 案例 01， myp01, myp02
  - import 模块 as 别名
    - 导入的同时给模块起一个别名
    - 其余用法跟第一种相同
    - 案例 3
  - from module_name import func_name, class_name
    - 案例 4
  - from module_name import *
    - 导入模块所有内容
    - 案例 5
- if __name__ == '__main__':  的使用
  - 可以有效避免模块代码被导入的时候被动执行的问题
  - 建议所有程序的入口都以为入口

模块的搜索路径和存储
- 什么是模块的搜索路径：
  - 加载模块时，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径
          import sys
          sys.path  属性可以获取路径列表
          # 案例 6
- 添加搜索路径
          sys.path.append(dir)
- 模块的加载顺序
  - 先搜索内存中已经加载好的模块
  - 搜索python的内置模块
  - 搜索sys.path路径

包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将萨凡纳七年五月底一起的文件夹就是包
- 自定义的结构
        包
        -- __init__.py   # 包的标志文件
        -- 模块1
        -- 模块2
        -- 子包
        -- | -- __init__.py  # 包的标志文件
        -- | -- 子包模块1
        -- | -- 子包模块2
- 包的导入操作
  - import package_name
    - 直接导入一个包，可以使用__init__.py中的内容
    - 使用方式是：
        package_name.func_name
        package_name.class_name.func_name
    - 此种方式的访问内容是
    - 案例 pkg01, myp02.py, 案例 7
  - import package_name as p
    - 具体用法跟作用试，跟上述简单导入一致
    - 注意的是此种方法是默认对__init__.py内容的导入
  - import package.module
    - 导入包中某一个具体的模块
    - 使用方法
          package.module.func_name
          package.module.class.fun()
          package.module.class.var
    - 案例 8
  - import package.module as pm
- from ... import 导入
  - from package import module1, module2, ...
  - 此种导入方法不执行 __init__  的内容
  - 用法
          form pkg01 import p01
          p01.sayHello()
  - from package import *
    - 导入当前包  ‘__init__.py’ 文件中所有的函数和类
    - 使用方法
        func_name()
        class_name.func_name()
        class_name.var
    - 案例 9， 注意此种导入的具体内容
- from package.module import *
  - 导入包中指定的模块的n所有内容
  - 使用方法 
        func_name()
        class_name.func_name()
- 在开发环境中经常会用其它模块，可以在当前包中直接导入其它模块中的内容
  - import 完整的包或者模块的路径
- '__all__' 的用法
  - 在使用 from package import * 的时候，* 可以导入的内容
  - ‘__init__.py’中如果文件为空，或者没有 "__all__"  ，那么只可以把__init__ 中的内容导入
  - __init__ 如果设置了 __all__的值 ，那么则按照__all__指定的子包或者模块进行进行加载，如此则不会载入 __init__ 中的内容
  - __all__ = ['module1', 'module2', 'package1', ...]
  - 案例 10

命名空间
- 用于区分不同位置不同功能但相同名称的函数 或者变量的一个特定前缀
- 作用是防止命名冲突
        setName()
        Student.setName()
        Dog.setName()
'''
