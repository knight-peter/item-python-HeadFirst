'''
重点：textvariable set()
把text参数替换成textvariable。如果你把一个特定的tkinter的变量赋予这个参数，那么当这个标签也会自动变化。使用“set()”方法来调整“IntVar”的值，然后GUI就会做相应的更新。
'''

# -*- conding: utf-8 -*-
# 从tkinter模块导入所有的功能=============================================================================================
from tkinter import *
import pygame.mixer


# 创建两个事件处理器，他们负责设置InVar和播放相应的声音=======================================================================
def num_total_change():
    num_total.set(num_correct.get()+num_wrong.get())
def play_correct_sound():
    num_correct.set(num_correct.get()+1)
    num_total_change()
    correct_s.play()

def play_wrong_sound():
    num_wrong.set(num_wrong.get()+1)
    num_total_change()
    wrong_s.play()

# 创建一个名为“app”的tkinter应用程序窗口===================================================================================
app = Tk()
# 给这个窗口起个名字
app.title("TVN Game Show")
# 指定窗口的坐标和尺寸值,geometery('高度x宽度+X坐标+Y坐标')
app.geometry('450x150+600+100')

# 初始化声音系统==========================================================================================================
sounds = pygame.mixer
sounds.init()

# 加载需要的声音==========================================================================================================
correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

# 创建两个IntVar:一个统计正确答案，另一个统计错误答案的个数===================================================================
num_total=IntVar()
num_total.set(0)
num_correct = IntVar()
num_correct.set(0)
num_wrong = IntVar()
num_wrong.set(0)

# 显示一个友好的消息，告诉主持人需要做什么。请确保你要放置（PACK）了你的窗口小部件
lab = Label(app, text='当你准备好了，请点击按钮！')
lab.pack()

# 创建两个标签来显示，并且把标签并且把标签与相对应的事件处理函数关联
lab1 = Label(app, textvariable=num_correct)
lab1.pack(side='left')

lab2 = Label(app, textvariable=num_wrong)
lab2.pack(side='right')

lab3=Label(app,textvariable=num_total)
lab3.pack(side='bottom')

# 创建每个按钮并把它们与相应的事件处理函数链接==============================================================================
# 为“Correct”事件创建一个按钮
b1 = Button(app, text="正确！", width=10, command=play_correct_sound)
# pack()方法把新创建的按钮链接到现有的窗口里
b1.pack(side='left', padx=10, pady=10)  # 把一个按钮放置在左边

# 为“Wrong”事件创建另一个按钮
b2 = Button(app, text="错误！", width=10, command=play_wrong_sound)
b2.pack(side='right', padx=10, pady=10)  # 把一个按钮放置在右边

# 开始tkinter的事件循环
app.mainloop()
