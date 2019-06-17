# 
"""
GUI介绍
- GraphicalUserInterface,
- GUI for Python: Tkinter, wxPython, PyQt
-TKinter
  - 绑定的是TK GUI工具集，用途Python包装的tTcl代码
-PyGTK
  - Tkinter的替代品
- wxPython
  - 跨平台的Python GUI
- PyQt
  - 跨平台
  - 商业授权可能有问题
- 推荐资料
  - 辛星GUI, 辛星Python
  - Python GUI Program cookbook
  - Tkinter reference a GUI for Python
"""
# Tkinter实例
import tkinter
tkinter._test()

import tkinter
base = tkinter.Tk()
base.mainloop()

"""
Tkinter 常用组件
- 按钮
    Button          按钮组件
    RadioButton     单选按钮组件
    CheckButton     选择按钮组件
    ListBox         列表组件
- 文本输入组件
    Entry       单选文本框组件
    Text        多行文本框组件
- 标签组件
    Label       可以显示图片和文字
    Message     可以根据内容将文字换行
- 菜单
    Menu        菜单组件
    MenuButton  菜单按钮组件
- 滚动条
    scale       滑块组件
    Scrollbar   滑动条组件
- 其它组件
    Canvas      画布组件
    Frame       框架组件，将多个组件编组
    Toplevel    创建子窗口窗口组件

组件大致使用步骤
1. 创建总面板
2. 创建面板上的各种组件
    1. 指定组件的交组件，即依附关系
    2. 利用相应的属性对组件进行设置
    3. 给组件安排布局
3. 同步骤2相似，创建好多个组件
4. 最后，启动总面板的消息循环
"""

#Label 的例子
import tkinter

base tkinter.Tk()
#负责标题
base .wm_title("Lable Test")

lb = tkinter.Label(base, text="Python Lable")
# 组组件指定布局
lob.pack()
# 消息循环
base.mainloop()


# 设置Label的例子
import tkinter

base = tkinter.Tk()
#负责标题
base .wm_title("Lable Test")

lb = tkinter.Label(base, text="Python Lable")
# 组组件指定布局
lob.pack()

lb2 = tkinter.Label(base, text="绿色背景", background="green")
lb2.pack()
# 消息循环
base.mainloop()

# Button的案例
import tkinter

def showLabel():
  global baseFrame
  lb = tkinter.Label(baseFrame, text="显示Label")
  lb.pack()

baseFrame = tkinter.Tk()
# 生成一个按钮
btn = tkinter.Button(baseFrame, text="show label", command=showLabel)
btn.pack()

baseFrame.mainloop()


"""
组件布局
- 控制组件的摆放方式
- 三种布局：
  - pack: 按照方位布局
    - 最简单，代码量最少， 挨个摆放
    - 通用使用方式为： 组件对象，pack(设置,,,,)
    - side: 依靠方位，可选值为LEFT,TOP,RIGHT,BOTTON
    - fill: 填充方式, X,Y,BOTH,NONE
    - expand: YES/NO
    - anchor: N, E, S, W, CENTER
    - ipadx: x方向的内边距
    - ipady: y方向的内边距
    - padx: x方向的外边距
    - pady: y方向的外边距
  - place: 按照坐标布局
    - 明确方位的摆放
    - 相对位置布局，随意改变窗口大小会导致混乱
    - 使用place函数，分为绝对布局和相对布局，绝对布局使用x,y参数
    - 相对布局使用relx, rely, relheight, relwidth
  - grid: 网格布局 -- Entry
    - 通用使用方式：组件对象，grid(设置,,,,,)
    - 利用row, column编号，都是从0开始
    - sticky: N, E, S, W, 表示上下左右，用来决定组件从哪个方向开始
    - 支持ipadx,padx等参数，跟pack函数含义一样
    - 支持span, columnspan,表示跨行，跨列数量
"""

# pack布局案例
import tkinter
baseFrame = tkinter.Tk()

btn1 = tkinter.Button(baseFrame, text='A')
btn1.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.Y)

btn2 = tkinter.Button(baseFrame, text='B')
btn2.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

btn3 = tkinter.Button(baseFrame, text='C')
btn3.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH, anchor=tkinter.NE)

baseFrame.mainloop()

# grid 布局bp案例
import tkinter
baseFrame = tkinter.Tk()

lb1 = tkinter.Label(baseFrame, text="账号：").grid(row=0, sticky=tkinter.W)
tkinter.Entry(baseFrame).grid(row=0, column=1, sticky=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="账号：").grid(row=1, sticky=tkinter.W)
tkinter.Entry(baseFrame).grid(row=1, column=1, sticky=tkinter.E)

btn = tkinter.Button(baseFrame, text="登录").grid(row=2, column=1, sticky=tkinter.W)

baseFrame.mainloop()

"""
消息机制
- 消息的传递r机制
  - 自动发出事件/消息
  - 消息有系统负责发送到队列
  - 由相关组件进行绑定/设置
  - 后端自动选择感兴趣的事件并做出相应反应
- 消息格式：
  - <[modifier-]---type-[-detail]>
  - <Button-1>: Button表示一个按钮事件，1wager是鼠标左键，2代表中键
  - <KeyPress-A>: 键盘A键位
  - <Control-Shift-KeyPress-A>:同时按下Control,Shift,A三个键位
  - [键位对应名称](https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html)
"""

# 事件的简单例子
import tkinter

def baseLabel(event):
  global baseFrame
  lb = tkinter.Label(baseFrame, text='谢谢点击')
  lb.pack()

# 画出程序的总框架
baseFrame = tkinter.Tk()
lb = tkinter.Label(baseFrame, text='模拟按钮')
# Label绑定相应的消息和处理函数
# 自动获取左键点击，并启动是难以的处理函数baseLabel
lb.bind("<Button-1>", baseLabel)
lb.pack()

# 启动消息循环
# 到此，表示程序开始运行
baseFrame.mainloop()


"""
Tkinter的绑定
- bind_all：全局范围的绑定，默认的是全局快捷键，比如F1是帮助文档
- bind_class: 接受三个参数，第一个是类名，第二个是事件，第三个是操作
  - w.bind_class('Entry', '<Control-V', my_paste)
- bine: 单独对某一个实例绑定
- unbind: 解绑， 需要一个参数，即要解绑哪个事件

Entry
- 输入框，功能单一
- entry["show"]="*, 设置适当字符
"""

# 输入框案例
import tkinter

def reg():
  # 从相应输入框中，得到用户的输入
  name = e1.get()
  pwd = e2.get()

  t1 = len(name)
  t2 = len(pwd)

  if name == "111" and pwd == "222":
    lb3["text"] = "登录成功"
  else:
    lb3["test"] = "用户名p账号或者密码错误"
    # 输入框删除掉用户输入的内容
    e1.delete(0, t1)
    e2.delete(0, t2)


baseFrame = tkinter.Tk()

lb1 = tkinter.Label(baseFrame, text="用户名")
lb1.grid(row=0, column=0, sticky=tkinter.W)

e1 = tkinter.Entry(baseFrame)
e1.grid(row=0, column=1, sticky=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="密码：")
lb2.grid(row=1, column=0, sticky=tkinter.W)

e2 = tkinter.Entry(baseFrame)
e2.grid(row=1, column=1, sticky=tkinter.E)

btn = tkinter.Button(baseFrame, text="登录", command=reg)
btn.grit(row=2, column=1, sticky=tkinter.E)

lb3 = tkinter.Label(baseFrame, text="")
lb3.grid(row=3)

baseFrame.mainloop()

"""
菜单
1. 普通菜单
- 第一个Menu类定义的是parent
- add_command 添加菜单项， 如果菜单是a顶层菜单，则从左向右添加，否则就是下拉菜单
  - label: 指定菜单项名称
  - command: 点击后十一日调用函数
  - acceletor: 快捷键
  - underline: 制定是否菜单信息下有横线
  - menu: 属性制定使用哪一个作为a顶级菜单
"""
# 普通菜单的代码
import tkinter

baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)

for item in ['File', 'Edit', 'View', 'About']:
  menubar.add_command(label=item)

baseFrame['menu'] = menubar
baseFrame.mainloop()

"""
级联菜单
- add_cascade: 级联资单， 作用是引出后面的菜单
- add_cascade的menu属性： 指明把菜单级联到哪个菜单上
- balel: 名称
- 过程：
  - 建立menu实例
  - add_command
  - add_cascade
"""
# 级联菜单实例
import  tkinter

baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)

emenu = tkinter.Menu(menubar)
for item in ['Copy', 'Pase', 'Cut']:
  emenu.add_command(label=item)

menubar.add_cascade(label='File')
menubar.add_cascade(label='Edit', menu=emenu)
menubar.add_cascade(label='About')

baseFrame['menu']=menubar

baseFrame.mainloop()

"""
弹出菜单
- 弹出菜单也叫上下文菜单
- 实现的大致思路
  - 建立菜单并向菜单添加各种功能
  - 监听鼠标右键
  - 如果右键点击，则根据位置判断弹出
  - 调用Menu的pop方法
- add_separator: 添加分隔符
"""
# 弹出菜单实例
import  tkinter

def makeLabel():
  global baseFrame
  tkinter.Label(baseFrame, text='PHP, Python').pack()

baseFrame = tkinter.Tk()
menubar = tkinter.Menu(baseFrame)

for x in ['麻辣香菇', '气锅鸡', '东坡肘子']:
  menubar.add_separator()
  menubar.add_command(label=x)

menubar.add_command(label='重庆火锅', command=makeLabel)

# 事件处理函数一定要至少有一个参数，h且第一个参数表示的是系统事件
def pop(event):
  menubar.post(event.x_root, event.y_root)

baseFrame.bind("<Button-3>", pop)
baseFrame.mainloop()


"""
canvas 画布
- 画布： 可以自由的在上面绘制图形的一个小舞台
- 在画布上绘制对象，通常用create_xxx, xxx=对象类型，例如Line, rectangle
- 画布的作用是把一定组件画到画布上显示出来
- 画布f所支持的组件：
  - arc 圆
  - bitmap
  - image(BitmapImage, PhotoImage)
  - line
  - polygon
  - rectangle
  - text
  - window(组件)
- 每次调用create_xx都会返回一个创建的组件的ID，同时也可以用tag属性指定其标签
- 通过调用canvas.move实现一个一次性动作
"""
# 画布实例
import  tkinter

baseFrame = tkinter.Tk()

cvs = tkinter.Canvas(baseFrame, width=300, height=400)
cvs.pack()

# 一条线需要两个点指明起止位置
cvs.create_lien(23, 23, 190, 234)
cvs.create_text(56, 67, text="i am python")

baseFrame.mainloop()


# 画一个五角星
import  tkinter
import math as m

baseFrame = tkinter.Tk()
# 创建一个多边形   create_polygon
baseFrame.mainloop()
