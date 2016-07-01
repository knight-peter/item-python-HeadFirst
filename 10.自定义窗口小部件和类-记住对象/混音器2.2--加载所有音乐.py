# -*- conding: utf-8 -*-
'''
WM_TAKE_FOCUS       当窗口在鼠标点击后被选中时给你的主窗口发送的消息
WM_SAVE_YOURSELF    当操作系统关闭时给你的主窗口发送的消息
WM_DELETE_WINDOW    当关闭框被点击时给你的主窗口发送的消息
'''
from tkinter import *
from sound_panel2 import *
import pygame.mixer
import os# 你需要跟操作系统打交道，所以导入“os”模块

# 创建GUI应用程序窗口
app = Tk()
app.title("混音器")

# 启动声音系统
mixer = pygame.mixer
mixer.init()

#获取当前目录下所有的文件
dirList=os.listdir(".")
# 取出每个文件名
for fname in dirList:
    # 如果它以“.wav”结尾的话
    if fname.endswith(".ogg"):
#         创建一个SoundPanel()并把它添加到GUI中
        panel=SoundPanel(app,mixer,fname)
        panel.pack()


# 当窗口关闭时要求歌曲停止播放4
def shutdown():
    app.destroy()  # destroy()销毁组件时触发


# 开始GUI事件循环
# 在调用“app.mainloop()”之前先调用“app.protocol()”
app.protocol("WM_DELETE_WINDOW", shutdown)  # 窗口被关闭时，调用“shuoMain”
app.mainloop()
