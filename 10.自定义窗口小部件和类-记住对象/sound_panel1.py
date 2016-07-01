from tkinter import *
import pygame

# 当这个函数被调用时，它需要三个参数
def create_gui(app,mixer,sound_file):
    # 这是“create_gui()”函数内的一个局部函数
    # “track_toggle”函数根据复选框的状态播放或者停止歌曲
    def track_toggle():
        if track_playing.get() == 1:
            track.play(loops=-1)
        else:
            # 这些代码需要在调用“app.mainloop()”之前加到你的程序中
            track.stop()
    # 这也是局部函数
    def change_volume(v):
        track.set_volume(volume.get())

    # 加载歌曲的声音文件
    track = mixer.Sound(sound_file)

    track_playing = IntVar()
    # 使用声音文件的名字作为复选框关联的文本
    track_button = Checkbutton(app, variable=track_playing, command=track_toggle, text=sound_file)
    track_button.pack(side='left', padx=10, pady=10)

    # 音量调节组件
    # 创建一个tkinter的DoubleVar变量。就像IntVar和StringVar那样，DoubleVar变量保存着一个“魔法”值，这次这个值是个浮数点
    volume = DoubleVar()
    volume.set(track.get_volume())
    volume_scale = Scale(variable=volume, from_=0.0, to=1.0, resolution=0.1, command=change_volume, label="音量",
                         orient=HORIZONTAL)
    volume_scale.pack(side='right', padx=10, pady=10)