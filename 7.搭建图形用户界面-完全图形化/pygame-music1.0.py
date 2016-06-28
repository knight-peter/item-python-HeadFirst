# -*- coding: utf-8 -*-
# 导入你需要使用的库--pygame
import pygame.mixer
# 创建一个“pygame.mixer”对象并且初始化声音系统
sounds=pygame.mixer
sounds.init()

# “wait_finish()”函数不断循环直到channel的“get_busy()”方法返回False
def wait_finish(channel):
    # “get_busy()方法检查声音师傅正在播放”
    while channel.get_busy():
        # “pass”是Python的一个组成部分，它不做任何事情
        pass

# 加载你希望播放的声音文件
s=sounds.Sound("correct.wav")
wait_finish(s.play())
s2=sounds.Sound("wrong.wav")# 设定和播放每一种声音
wait_finish(s2.play())
s3=sounds.Sound("7420.wav")
wait_finish(s3.play())
