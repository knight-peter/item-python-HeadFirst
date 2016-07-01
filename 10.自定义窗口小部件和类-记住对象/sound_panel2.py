from tkinter import *
import pygame.mixer

# 当这个函数被调用时，它需要三个参数
class SoundPanel(Frame):
    # 首先是初始化方法。注意这个方法在Python中必须命名为“__init__()”,这样可以在对象创建时被自动调用。
    def __init__(self,app,mixer,sound_file):
        Frame.__init__(self,app)
        self.track=mixer.Sound(sound_file)
        self.track_playing=IntVar()
        track_button=Checkbutton(self,variable=self.track_playing,command=self.track_toggle,text=sound_file)
        track_button.pack(side='left',padx=10,pady=10)

        self.volume=DoubleVar()
        self.volume.set(self.track.get_volume())

        volume_scale=Scale(self,variable=self.volume,from_=0.0,to=1.0,resolution=0.1,command=self.change_volume,label="音量",orient=HORIZONTAL)
        volume_scale.pack(side='right')


    # 这是“create_gui()”函数内的一个局部函数
    # “track_toggle”函数根据复选框的状态播放或者停止歌曲
    def track_toggle(self):
        if self.track_playing.get() == 1:
            self.track.play(loops=-1)
        else:
            # 这些代码需要在调用“app.mainloop()”之前加到你的程序中
            self.track.stop()
    # 这也是局部函数
    def change_volume(self,v):
        self.track.set_volume(self.volume.get())
