#这两行代码用来生成随机数
from random import randint
secret=randint(1,10)
print("欢迎，这是一个猜数字游戏。")
guess=0
'''
检查答案是否等于那个secret变量中设定的随机数。
'''
while guess!=secret:
    g=input("请输入一个数字：")
    guess=int(g)
    if guess==secret:
        print("你猜对了！")
    else:
        if guess>secret:
            print("太高了")
        else:
            print("太低了")
print("游戏结束。")