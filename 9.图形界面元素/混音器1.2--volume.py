# -*- conding: utf-8 -*-
'''
WM_TAKE_FOCUS       当窗口在鼠标点击后被选中时给你的主窗口发送的消息
WM_SAVE_YOURSELF    当操作系统关闭时给你的主窗口发送的消息
WM_DELETE_WINDOW    当关闭框被点击时给你的主窗口发送的消息
'''
from tkinter import *
import pygame.mixer
from tkinter.messagebox import askokcancel  # 导入异常状态框

# 创建GUI应用程序窗口
app = Tk()
app.title("混音器")
# app.geometry('250x100+200+100')

# 确认DJ的歌曲
sound_file = "nnkf-xynq.ogg"
# 启动声音系统
mixer = pygame.mixer
mixer.init()


# “track_toggle”函数根据复选框的状态播放或者停止歌曲
def track_toggle():
    if track_playing.get() == 1:
        track.play(loops=-1)
    else:
        # 这些代码需要在调用“app.mainloop()”之前加到你的程序中
        track.stop()


def change_volume(v):
    track.set_volume(volume.get())


# 加载歌曲的声音文件
track = mixer.Sound(sound_file)

track_playing = IntVar()
# 使用声音文件的名字作为复选框关联的文本
track_button = Checkbutton(app, variable=track_playing, command=track_toggle, text=sound_file)
track_button.pack(side='left',padx=10,pady=10)


# 音量调节组件
# 创建一个tkinter的DoubleVar变量。就像IntVar和StringVar那样，DoubleVar变量保存着一个“魔法”值，这次这个值是个浮数点
volume=DoubleVar()
volume.set(track.get_volume())
volume_scale=Scale(variable=volume,from_=0.0,to=1.0,resolution=0.1,command=change_volume,label="音量",orient=HORIZONTAL)
volume_scale.pack(side='right',padx=10,pady=10)


# 当窗口关闭时要求歌曲停止播放
def shutdown():
    if askokcancel(title='你确定？', message='你想要离开吗？'):
        app.destroy()  # destroy()销毁组件时触发



# 开始GUI事件循环
# 在调用“app.mainloop()”之前先调用“app.protocol()”
app.protocol("WM_DELETE_WINDOW", shutdown)  # 窗口被关闭时，调用“shuoMain”
app.mainloop()
