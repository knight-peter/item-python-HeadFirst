# -*- conding: utf-8 -*-
'''
WM_TAKE_FOCUS       当窗口在鼠标点击后被选中时给你的主窗口发送的消息
WM_SAVE_YOURSELF    当操作系统关闭时给你的主窗口发送的消息
WM_DELETE_WINDOW    当关闭框被点击时给你的主窗口发送的消息
'''
from tkinter import *
from tkinter.messagebox import askokcancel  # 导入异常状态框
from sound_panel1 import *
import pygame.mixer

# 创建GUI应用程序窗口
app = Tk()
app.title("混音器")

# 启动声音系统
mixer = pygame.mixer
mixer.init()

create_gui(app,mixer,'nnkf-xynq.ogg')
create_gui(app,mixer,'qhc.ogg')

# 当窗口关闭时要求歌曲停止播放
def shutdown():
    if askokcancel(title='你确定？', message='你想要离开吗？'):
        app.destroy()  # destroy()销毁组件时触发


# 开始GUI事件循环
# 在调用“app.mainloop()”之前先调用“app.protocol()”
app.protocol("WM_DELETE_WINDOW", shutdown)  # 窗口被关闭时，调用“shuoMain”
app.mainloop()
