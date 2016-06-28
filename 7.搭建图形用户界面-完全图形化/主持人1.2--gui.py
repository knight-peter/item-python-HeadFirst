'''
通过command参数链接函数
'''

# -*- conding: utf-8 -*-
# 从tkinter模块导入所有的功能
from tkinter import *

import pygame.mixer

sounds=pygame.mixer
sounds.init()

correct_s=sounds.Sound("correct.wav")
wrong_s=sounds.Sound("wrong.wav")

number_correct=0
number_wrong=0

# Python的"global"关键字允许你更改一个在函数之外创建的变量的值
def play_correct_sound():
    global number_correct
    number_correct=number_correct+1
    correct_s.play()

def play_wrong_sound():
    global number_wrong
    number_wrong=number_wrong+1
    wrong_s.play()

# 创建一个名为“app”的tkinter应用程序窗口
app = Tk()
# 给这个窗口起个名字
app.title("你的GUI窗口")
# 指定窗口的坐标和尺寸值,geometery('高度x宽度+X坐标+Y坐标')
app.geometry('450x150+600+100')
# 为“Correct”事件创建一个按钮
b1 = Button(app, text="正确！", width=10,command=play_correct_sound)
# pack()方法把新创建的按钮链接到现有的窗口里
b1.pack(side='left', padx=10, pady=10)  # 把一个按钮放置在左边

# 为“Wrong”事件创建另一个按钮
b2 = Button(app, text="错误！", width=10,command=play_wrong_sound)
b2.pack(side='right', padx=10, pady=10)  # 把一个按钮放置在右边

# 开始tkinter的事件循环
app.mainloop()
