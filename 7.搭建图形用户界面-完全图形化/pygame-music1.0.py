# 导入你需要使用的库
import pygame.mixer
sounds=pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass

s=sounds.Sound("a.mp3")
wait_finish(s.play())
s2=sounds.Sound("b.mp3")
wait_finish(s2.play())
s3=sounds.Sound("c.mp3")
wait_finish(s3.play())