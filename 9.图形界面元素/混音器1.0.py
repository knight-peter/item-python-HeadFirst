# -*- conding: utf-8 -*-
'''
WM_TAKE_FOCUS       当窗口在鼠标点击后被选中时给你的主窗口发送的消息
WM_SAVE_YOURSELF    当操作系统关闭时给你的主窗口发送的消息
WM_DELETE_WINDOW    当关闭框被点击时给你的主窗口发送的消息
'''
from tkinter import *
import pygame.mixer
# 导入异常状态框
from tkinter.messagebox import askokcancel

# 创建GUI应用程序窗口
app = Tk()
app.title("混音器")
app.geometry('250x100+200+100')
# 确认DJ的歌曲
sound_file = "nnkf-xynq.ogg"
# 启动声音系统
mixer = pygame.mixer
mixer.init()


# “track_start()”函数将响应“Start”按钮点击事件
def track_start():
    # “play()”的“loops=-1”参数重复播放这首歌曲直到你停止它
    track.play(loops=-1)


def track_stop():
    track.stop()


# 当窗口关闭时只要求歌曲停止播放
def shutdown():
    if askokcancel(title='你确定？',message='你想要离开吗？'):
        app.destroy()


#     加载歌曲的声音文件
track = mixer.Sound(sound_file)
# 为“Start”和“Stop”创建按钮，然后把它们与各自的事件处理器相联系
start_button = Button(app, command=track_start, text="开始")
start_button.pack(side='left',padx=10)
stop_button = Button(app, command=track_stop, text="停止")
stop_button.pack(side='right',padx=10)
# 开始GUI事件循环
# 在调用“app.mainloop()”之前先调用“app.protocol()”
app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
