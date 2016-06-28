# -*- conding: utf-8 -*-
# 为了播放声音，你需要导入pygame的"mixer"模块
import pygame.mixer


# 让声音连续播放
def wait_finish(channel):
    while channel.get_busy():
        pass


# 创建一个mixer对象，并且初始化pygame的声音系统
sounds = pygame.mixer
sounds.init()

# 把每个需要播放的声音加载到它对应的变量里
correct_s = sounds.Sound("correct.wav")  # 答题正确的音效
wrong_s = sounds.Sound("wrong.wav")  # 答题错误的音效

# 这是每次需要询问主持人的问题
prompt = "按1选择正确，按2选择错误，或者按0选择退出："

# 确保你需要维护的计数器被设置了一个合理的初始值
# 把这三行移到程序的头部也没有问题，制药他们在while循环之前被赋予了初始值
number_asked = 0
number_correct = 0
number_wrong = 0

# 提示主持人
choice=input(prompt)
# 当游戏还没有被选择退出时
while choice !='0':
    # 如果回答是正确的，增加计数器的值并且播放相应的声音。
    if choice=='1':
        number_asked=number_asked+1
        number_correct=number_correct+1
        wait_finish(correct_s.play())
    # 如果回答是错误的，增加计数器的值并且播放相应的声音
    if choice=='2':
        number_asked=number_asked+1
        number_wrong=number_wrong+1
        wait_finish(wrong_s.play())
    choice=input(prompt)

# 在程序结尾，显示计数器值的总和
print("你问了"+str(number_asked)+"个问题。")
print(str(number_correct)+"个问题是正确的。")
print(str(number_wrong)+"个问题是错误的。")
